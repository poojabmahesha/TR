#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

try:
    from pip._internal import download, req
except ImportError:
    # for pip < 10.0.0
    from pip import req, download
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


parsed_requirements = req.parse_requirements(
    'requirements.txt',
    session=download.PipSession()
)

parsed_test_requirements = req.parse_requirements(
    'requirements_dev.txt',
    session=download.PipSession()
)

requirements = [str(ir.req) for ir in parsed_requirements]
setup_requirements = [
    'setuptools_scm',
    # TODO(fcorone2): put setup requirements
    # (distutils extensions, etc.) here
]
test_requirements = [str(tr.req) for tr in parsed_test_requirements]

setup(
    name='treerunner_lib',
    use_scm_version=True,
    description="EDIS Treerunner Lib",
    long_description=readme + '\n\n' + history,
    author="Flavio Coronel",
    author_email='fcorone2@ford.com',
    url='https://github.ford.com/fcorone2/treerunner_lib',
    packages=find_packages(include=['treerunner_lib']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='treerunner_lib',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
