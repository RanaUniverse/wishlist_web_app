# gunicorn.conf.py

# i will want to take the app_port value form the env


import multiprocessing
import os

port_value = os.getenv(key="APP_PORT")
workers = os.getenv(key="GUNICORN_WORKERS")
threads = os.getenv(key="GUNICORN_THREADS")


DEFAULT_PORT = 9999
DEFAULT_WORKERS = multiprocessing.cpu_count()
DEFAULT_THREADS = 2


# Port
port_value = os.getenv("APP_PORT")
if port_value is None:
    port_value = DEFAULT_PORT
    print("APP_PORT not set. Using default: 9999")
else:
    port_value = int(port_value)


# Workers
workers = os.getenv("GUNICORN_WORKERS")
if workers is None:
    workers = DEFAULT_WORKERS
    print(f"GUNICORN_WORKERS not set. Using default: {workers}")
else:
    workers = int(workers)


# Threads
threads = os.getenv("GUNICORN_THREADS")
if threads is None:
    threads = 2
    print(f"GUNICORN_THREADS not set. Using default: {threads}")
else:
    threads = int(threads)


bind = f"0.0.0.0:{port_value}"

timeout = 60
max_requests = 2000
max_requests_jitter = 100
preload_app = True
# This upper prload will help to reduct ram by copy already runned fork
