#!/bin/bash
docker-compose down
docker volume rm bodia_bodia-development-search-postgresql
docker-compose up -d --build --force-recreate --renew-anon-volumes bodia-development-search-postgresql
docker-compose up -d
docker-compose exec bodia-development-main python manage.py migrate --database=search_replicas
docker-compose exec bodia-development-main python manage.py reindex_company_replicas

