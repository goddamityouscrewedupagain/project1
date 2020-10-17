from django.core.management.base import BaseCommand

from search_replicas.models import CompanySearchReplica


class Command(BaseCommand):
    help = 'clear CompanySearchReplica'

    def handle(self, *args, **options):
        company_replicas_count = CompanySearchReplica.objects.count()
        CompanySearchReplica.objects.all().delete()
        msg = f'Successfully deleted company_replicas: {company_replicas_count}'
        self.stdout.write(self.style.SUCCESS(msg))
