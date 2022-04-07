from setuptools import setup, setuptools

setup(
    name='pl_api',
    version='0.0.1',
    author='Carlo Grigioni and Christian Pala',
    author_email='carlo.grigioni@student.supsi.ch, christian.pala@student.supsi.ch',
    description='client library for our API',
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    install_requires=['datetime', 'requests'],
    python_requires='>=3.8'
    )