# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='spotiapi',
    version='2.0.0',
    author='Julheer',
    author_email='admin@julheer.ru',
    description='A small Spotify API that can help you get the data of the user who issued the token.',
    long_description=open('./README.md', 'r', encoding="utf8").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/julheer/spotiapi',
    license='MIT',
    install_requires=['http3'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)
