web: gunicorn cn_django_test.wsgi:application --log-level=debug
celeryapp: celery -A kuberns.celery:kuberns_celery_app worker -l info -Q kuberns_celery_queue
celeryapp-2: celeryapp: celery -A kuberns.celery:kuberns_celery_app worker -l info -Q kuberns_celery_queue
