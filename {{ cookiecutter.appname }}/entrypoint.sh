#!/bin/sh

python /test_alive.py
flask db init
flask db migrate
flask db upgrade

gunicorn app:app --bind 0.0.0.0:5001