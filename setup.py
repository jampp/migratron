# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(setup_dir, 'db_utils', 'VERSION'), 'r') as vf:
    version = vf.read().strip()


def parse_requirements_txt(filename='requirements.txt'):
    requirements = open(os.path.join(os.path.dirname(__file__), filename)).readlines()
    # remove whitespaces
    requirements = [line.strip().replace(' ', '') for line in requirements]
    # remove all the requirements that are comments
    requirements = [line for line in requirements if not line.startswith('#')]
    # remove empty lines
    requirements = list(filter(None, requirements))
    return requirements


setup(
    name='db-utils',
    version=version,
    description='Run the database migrations',
    author='Jampp',
    install_requires=parse_requirements_txt(),
    entry_points={
        'console_scripts': {
            'db-utils = db_utils.main:main'
        }
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    package_data={'': ['VERSION']},
    test_suite='tests',
)
