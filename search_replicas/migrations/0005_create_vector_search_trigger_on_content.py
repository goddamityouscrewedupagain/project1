# Generated by Django 2.2.8 on 2020-04-27 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_replicas', '0004_create_vector_search_trigger'),
    ]

    migration = '''
                CREATE TRIGGER content_search_update BEFORE INSERT OR UPDATE
                ON search_replicas_companysearchreplica FOR EACH ROW EXECUTE FUNCTION
                tsvector_update_trigger(content_vector, 'pg_catalog.english', content);

                UPDATE search_replicas_companysearchreplica set ID = ID;
            '''

    reverse_migration = '''
                DROP TRIGGER content_search_update ON search_replicas_companysearchreplica;
        '''

    operations = [
        migrations.RunSQL(migration, reverse_migration)
    ]

