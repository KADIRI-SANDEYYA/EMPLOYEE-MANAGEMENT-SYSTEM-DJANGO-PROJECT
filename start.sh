#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn EMPLOYEE_MANAGEMENT_SYSTEM.wsgi:application --bind 0.0.0.0:$PORT

