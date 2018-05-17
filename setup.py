from setuptools import setup, find_packages

setup(
    name='configtools',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'pyyaml',
        'wrapt',
    ],
)
