

from setuptools import setup, find_packages
from os import path

setup(
    name='tsp',
    version='0.1.7',
    author='Bruno Casella',
    author_email='brunocasella@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data={'tsp': ['*.csv']},
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=['numpy'],
    scripts = ["scripts/tsp"],


)
