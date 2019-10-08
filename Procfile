web: gunicorn payres_backend.wsgi --log-file -
release: python manage.py migrate
release: python manage.py loaddata initial-data.json