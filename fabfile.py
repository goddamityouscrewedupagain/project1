from fabric.api import *


@task
def dev():
    env.user = 'web'
    env.hosts = ['49.12.69.117:2234']
    env.forward_agent = True


@task
def deploy():
    with cd('/web/bodia/'):
        run('pwd')
        run('git pull')
        run('docker-compose -f docker-compose.sandbox.yml down')
        run('docker-compose -f docker-compose.sandbox.yml up -d')
        run('docker-compose -f docker-compose.sandbox.yml exec bodia-sandbox-django python '
            'manage.py collectstatic --no-input --clear')
