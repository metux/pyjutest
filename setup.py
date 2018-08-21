#!/usr/bin/env python3

from distutils.core import setup

from pyju.version import pyju_version

setup(name='pyjutest',
      version=pyju_version,
      description='junit xml generator',
      author='Manuel Traut',
      author_email='manut@linutronix.de',
      url='http://mecka.net/',
      packages=['pyju'],
      scripts=['pyjutest'],
)
