# -*- coding: utf-8 -*-

__authors__ = (
    'Mark Hartney',
    'Chris Stevens',
)
__maintainer__ = 'Chris Stevens'
__email__ = 'connect@quandl.com'
__url__ = 'http://www.quandl.com/'
__license__ = 'MIT'
__version__ = '2.8.6'
#############################################
#
# Don't import anything in __init__.py!
# Otherwise setup.py can't import the private constants above (__authors__, etc)
# because it won't have installed dependencies yet!
#

# Perso modif
from .Quandl import (
    get,
    get_meta,
    push,
    search,
    WrongFormat,
    MultisetLimit,
    ParsingError,
    CallLimitExceeded,
    DatasetNotFound,
    ErrorDownloading,
    MissingToken,
    DateNotRecognized,
    CodeFormatError
    )

###############################################
