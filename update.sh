#!/bin/bash

git pull
docker-compose -f docker-compose.sandbox.yml down
docker-compose -f docker-compose.sandbox.yml up -d
docker-compose -f docker-compose.sandbox.yml exec bodia-sandbox-django python manage.py collectstatic --no-input --clear