start: ## start server
	docker-compose -f docker-compose.sandbox.yml up -d
stop: ## stop server
	docker-compose -f docker-compose.sandbox.yml down
collect_static: ## collectstatic
	docker-compose -f docker-compose.sandbox.yml exec bodia-sandbox-django python manage.py collectstatic --no-input --clear
pull:   ## git pull
	git pull
restart: stop start  ## restart server


## build on dev server
build_dev: pull restart collect_static  ## restart with collectstatic
build_dev_simple: pull restart  ## simple restart without collectstatic


## local
test:
	docker-compose run --rm bodia-development-main coverage run manage.py test main
report:  # only after 'test' execution
	docker-compose run --rm bodia-development-main coverage report
coverage:
	docker-compose run --rm bodia-development-main coverage html
	open ./htmlcov/index.html

