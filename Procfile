release: python manage.py migrate --run-syncdb && python manage.py loaddata initial-data.json
web: gunicorn payres_backend.wsgi --log-file -