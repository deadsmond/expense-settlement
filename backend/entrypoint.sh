#!/bin/sh

# Wait for DB to be ready
while ! nc -z $DB_HOST $DB_PORT; do
  echo "Waiting for database..."
  sleep 2
done

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn backend.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --log-level info
