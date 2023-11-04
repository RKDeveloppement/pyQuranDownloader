from setuptools import setup, find_packages

setup(
    name='pyQuranDownloader',
    version='1.0.1',
    author='RKDev',
    description='A simple module written in Python3 that allows you to download and manage quran of multiple reciters from mp3quran.net',
    packages=find_packages(),
    install_requires=[
        'urllib3'
    ]
)