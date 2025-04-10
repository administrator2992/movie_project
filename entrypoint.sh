#!/bin/sh
set -e

# Create database if missing
if [ ! -f "/app/db.sqlite3" ]; then
    touch "/app/db.sqlite3"
    echo "Created new SQLite database"
fi

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput --clear

# Start server
exec gunicorn --bind 0.0.0.0:8000 --workers 3 movie_project.wsgi:application
