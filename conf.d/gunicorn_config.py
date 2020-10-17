#  gunicorn --bind  --worker-tmp-dir /dev/shm --workers=2 --threads=4 --worker-class=gthread bodia.wsgi
from prometheus_client import multiprocess

bind = "unix:///web/app/django.sock"
worker_tmp_dir = "/dev/shm"
workers = 2
threads = 4
worker_class = "gthread"


def child_exit(server, worker):
    multiprocess.mark_process_dead(worker.pid)
