#!/bin/sh

python /test_alive.py

gunicorn app:app --bind 0.0.0.0:5001