 
release: python manage.py migrate
web: gunicorn aplicativo.wsgi:application --bind 0.0.0.0:$PORT
