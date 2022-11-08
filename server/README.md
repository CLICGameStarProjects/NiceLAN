# NiceLAN - Server

## Setup

Please follow the [main setup](../README.md). Then:

1. `cd server/nicelan`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py createsuperuser` and follow the instructions

## Usage

Simply do `python manage.py runserver 8765` then go to http://127.0.0.1:8765.
