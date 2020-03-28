python3 manage.py collectstatic --no-input
gunicorn Vibely.wsgi
