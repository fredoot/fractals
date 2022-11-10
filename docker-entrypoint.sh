#!/bin/bash

echo "***Docker entrypoint.sh***"
echo "***Migrate...***"
python manage.py migrate

echo "***Checking superuser..***"
python manage.py ensure_superuser --username admin --email admin@fractals.com --password admin

echo "***Starting server...***"
python manage.py runserver 0.0.0.0:8000