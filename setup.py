#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='shopxpress-ecommerce',
    version='1.0.0',
    description='Modern e-commerce platform with Django, Tailwind CSS and Material Design',
    author='ShopXpress Team',
    python_requires='>=3.12',
    packages=find_packages(include=['core']),
    install_requires=[
        'Django>=6.0.2,<7.0',
        'djangorestframework>=3.14.0',
        'python-decouple>=3.8',
        'gunicorn>=21.2.0',
        'whitenoise>=6.5.0',
        'psycopg2-binary>=2.9.9',
    ],
    include_package_data=True,
    zip_safe=False,
)
