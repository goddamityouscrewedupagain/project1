#!/bin/bash
docker-compose -f docker-compose.sandbox.yml down
docker volume rm bodia_bodia-sandbox-search-postgresql
docker-compose -f docker-compose.sandbox.yml up -d --build --force-recreate --renew-anon-volumes bodia-sandbox-search-postgresql
docker-compose -f docker-compose.sandbox.yml up -d
docker-compose -f docker-compose.sandbox.yml exec bodia-sandbox-django python manage.py migrate --database=search_replicas
docker-compose -f docker-compose.sandbox.yml exec bodia-sandbox-django python manage.py reindex_company_replicas

