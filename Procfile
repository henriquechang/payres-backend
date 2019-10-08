release: python manage.py migrate && python manage.py loaddata initial-data.json
web: gunicorn payres_backend.wsgi --log-file -