#!/usr/bin/env python3

from distutils.core import setup
from msrplib import __version__

setup(
    name='python3-msrplib',
    version=__version__,
    author='AG Projects',
    author_email='support@ag-projects.com',
    license='LGPL',
    description='Client library for MSRP protocol and its relay extension (RFC 4975 and RFC4976)',
    url='http://msrprelay.org',
    packages=['msrplib']
)
