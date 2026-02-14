#!/bin/bash

# Collect static files
python manage.py collectstatic --no-input

# Run migrations (if needed)
python manage.py migrate --no-input
