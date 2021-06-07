#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup, find_packages
import shop

with open('README.md', 'r') as fh:
    long_description = fh.read()

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
    'Framework :: Django :: 2.1',
    'Framework :: Django :: 2.2',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Jacob Rief",
    author_email="jacob.rief@gmail.com",
    name="django-ngoshop",
    version=shop.__version__,
    description="A RESTful e-commerce framework based on Django (django-shop fork)",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://www.django-shop.org/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=2.1,<3.0',
        'django-post_office>=3.2.0',
        'django-filer>=1.4',
        'django-ipware>=1.1.1',
        'django-fsm>=2.4.0',
        'django-fsm-admin>=1.2.4',
        'djangorestframework>3.8',
        'django-angular>2.2',
        'Django-Select2<7',
        'django-rest-auth',
        'django-admin-sortable2>=0.7.4',
        'django-formtools>1.0',
        'djangocms-cascade>1.1',
        'django-coupons==1.1.0',
    ],
)
