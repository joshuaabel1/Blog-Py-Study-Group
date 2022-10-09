#!/usr/bin/env bash
# exit on error

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
# python manage.py createsuperuser --email=admin1@admin.com --noinput