#!/usr/bin/env bash
# exit on error

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
# python manage.py makemigrations Blog
python manage.py migrate
# python manage.py createsuperuser --email=admin1@admin.com --noinput