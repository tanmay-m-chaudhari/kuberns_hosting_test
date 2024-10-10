web: gunicorn cn_django_test.wsgi:application --log-level=debug
celeryapp-2: celery -A kuberns.celery:kuberns_celery_app worker -l info -Q kuberns_celery_queue
celeryapp: celeryapp: celery -A kuberns.celery:kuberns_celery_app worker -l info -Q kuberns_celery_queue
