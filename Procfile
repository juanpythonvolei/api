
release: python manage.py makemigrations api_engine
release: python manage.py migrate
web: gunicorn api.wsgi:application --bind 0.0.0.0:$PORT
