#!/bin/bash

echo "The current directory is:"
pwd

virtualenv myenv
source myenv/bin/activate

pip install -U pip
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver