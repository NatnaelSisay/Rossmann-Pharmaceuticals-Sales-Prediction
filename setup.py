#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirement_file:
    requirements_list = requirement_file.readlines()
    requirements_list = [lib.replace('\n', '') for lib in requirements_list]

requirements = requirements_list

test_requirements = []

setup(
    author="Natnael Sisay",
    author_email="natyjava8@gmail.com",
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Prediction for Rossmann Pharmaceuticals",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='Rossmann Prediction',
    name='Rossmann Prediction',
    packages=find_packages(include=['myscripts', 'myscripts.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/DePacifier/SmartAd-Campaign',
    version='0.1.0',
    zip_safe=False,
)