"""
Celery configurations file
"""

from os import environ

CELERY_BROKER_URL = environ["CELERY_BROKER_URL"]
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "max_retries": environ.get("CELERY_PUBLISH_MAX_RETRIES", 1)
}
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERY_IGNORE_RESULT = False
CELERY_SEND_EVENTS = True
DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH = 100
