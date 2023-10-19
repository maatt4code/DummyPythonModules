#!/usr/bin/env python

from distutils.core import setup

setup(name='hellopython',
      version='1.0',
      description='Dumb function to make console print hello',
      author='My Name',
      author_email='my.name.is.wa@wa.co',
      url='TBC',
      packages=['hellopython'],
      # Additional required python packages.
      # Latest will be installed if not in requirements.txt
      install_requires=['matplotlib'],
      # what to expose as callable as a bash command
      entry_points={'console_scripts': [
        'maatt-print_hello = hellopython.hello:dummy_print_hello']}
     )
