#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
import sys, os

VERSION = '0.1.0'

with open('README.md') as f:
    long_description = f.read()

setup(
      name='NCTU-Oauth',
      version=VERSION,
      description="adds NCTU-Oauth support to flask",
      long_description=long_description,
      classifiers=[],
      keywords='python flask nctu oauth nctu-oauth',
      author='steven5538',
      author_email='steven5538@gmail.com',
      url='https://github.com/steven5538/NCTU-Oauth',
      license='BSD',
      packages=['nctu_oauth'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'requests',
		'pyOpenSSL',
		'ndg-httpsclient',
		'flask'
      ],
)

