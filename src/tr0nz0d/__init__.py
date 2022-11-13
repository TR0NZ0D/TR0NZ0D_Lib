# -*- coding: utf-8 -*-

"""
TR0NZ0D Utils Library
~~~~~~~~~~~~~~~~~~~

Library created to facilitate the access and usage of common tools.

:copyright: (c) 2021 TR0NZ0D
:license: MIT, see LICENSE for more details.

"""

__title__ = 'tr0nz0d'
__author__ = 'TR0NZ0D'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 TR0NZ0D'
__version__ = '0.1.4'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# Imports
import logging

# Instances
logging.getLogger(__name__).addHandler(logging.NullHandler())
