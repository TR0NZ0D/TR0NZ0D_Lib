# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import logging
from typing import Any
from enum import Enum


class LoggingLevels(Enum):
    """ Logging levels, use just static references """
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0


class Log:
    class __Formatter(logging.Formatter):
        grey: str = "\x1b[38;20m"
        bold_grey: str = "\x1b[30;1m"
        yellow: str = "\x1b[33;20m"
        red: str = "\x1b[31;20m"
        bold_red: str = "\x1b[31;1m"
        reset: str = "\x1b[0m"
        blue: str = '\x1b[33;94m'
        cyan: str = '\x1b[33;96m'
        green: str = '\x1b[33;92m'
        white: str = '\x1b[33;37m'
        text_format = "%(asctime)s [%(levelname)s]: "  # NOQA:E501
        message = white + "%(message)s" + reset

        FORMATS = {
            logging.DEBUG: green + text_format + reset + message,
            logging.INFO: blue + text_format + reset + message,
            logging.WARNING: yellow + text_format + reset + message,
            logging.ERROR: red + text_format + reset + message,
            logging.CRITICAL: bold_red + text_format + reset + message,
            logging.NOTSET: cyan + text_format + reset + message
        }

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt)
            return formatter.format(record)

    def __init__(self, level: LoggingLevels) -> None:
        self.__logger__ = logging.getLogger()
        self.__logger__.setLevel(level.value)
        log_handler = logging.StreamHandler()
        log_handler.setLevel(level.value)
        log_handler.setFormatter(self.__Formatter())
        self.__logger__.addHandler(log_handler)

    def warning(self, content: Any) -> None:
        """ Logs a message in warning level

        Args:
            content (Any): Message to be logged
        """
        self.__logger__.warning(content)

    def debug(self, content: Any) -> None:
        """ Logs a message in debug level

        Args:
            content (Any): Message to be logged
        """
        self.__logger__.debug(content)

    def error(self, content: Any) -> None:
        """ Logs a message in error level

        Args:
            content (Any): Message to be logged
        """
        self.__logger__.error(content)

    def info(self, content: Any) -> None:
        """ Logs a message in info level

        Args:
            content (Any): Message to be logged
        """
        self.__logger__.info(content)

    def critical(self, content: Any) -> None:
        """ Logs a message in critical level

        Args:
            content (Any): Message to be logged
        """
        self.__logger__.critical(content)
