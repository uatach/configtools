from os import path
from setuptools import setup, find_packages

import configtools


project_name = configtools.__name__
project_version = configtools.__version__

project_dir = path.abspath(path.dirname(__file__))

with open(path.join(project_dir, 'README.md')) as fp:
    long_description = fp.read()


setup(
    name=project_name,
    version=project_version,
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='edson duarte',
    author_email='',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='',

    packages=find_packages(exclude=['tests']),
    install_requires=[
        'pyyaml',
        'wrapt',
    ],

    project_urls={
        'Bug Reports': f'https://github.com/uatach/{project_name}/issues',
        'Source': 'https://github.com/uatach/{project_name}/',
    },
)
