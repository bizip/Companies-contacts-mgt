# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in company_contacts/__init__.py
from company_contacts import __version__ as version

setup(
	name='company_contacts',
	version=version,
	description='Managing the contacts for the companies',
	author='Bizimungu pascal',
	author_email='bizip04@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
