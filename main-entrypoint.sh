#!/bin/sh

set -x
set -e

python manage.py runserver 127.0.0.1:8000
