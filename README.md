# To run project please use following articles
development – https://gitlab.com/dteam.dev/bodia/-/wikis/create_development_environment

sandbox - ???

production - ???


# dev install

```
cp .env.example .env
docker-compose build
docker-compose up -d
docker exec -i bodia_bodia-development-main-postgresql_1 psql -U main-db-user -d main-db-name < ~/Dropbox/backup/bodia_backup_20200422_225404_backup.sql
docker-compose exec bodia-development-main python manage.py migrate
docker-compose exec bodia-development-main python manage.py createsuperuser
docker-compose exec bodia-development-main python manage.py migrate --database=search_replicas
docker-compose exec bodia-development-main python manage.py reindex_company_replicas
```

go to http://localhost:8001/ and http://localhost:8001/admin
