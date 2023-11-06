#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Creating a virtual env for both poetry and our packages..."
python -m venv venv

echo "Updating pip ;-)..."
/opt/render/project/src/.venv/bin/python3.9 -m pip install --upgrade pip


echo "Installing new/better version of poetry into our virtual env..."
./venv/bin/pip install poetry==1.6.1

echo "Installing django into our virtual env..."
pip install Django
pip install dj-database-url
pip install psycopg2-binary
pip install 'whitenoise[brotli]'
pip install gunicorn

echo "Done"

python manage.py collectstatic --no-input
python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input