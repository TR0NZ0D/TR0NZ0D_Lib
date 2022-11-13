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

from typing import Dict, List, Optional, TypeVar

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')


def get_first(container: Dict[K, V]) -> Optional[K]:  # type: ignore
    """ Returns the first key from the dict container

    Args:
        container (Dict[K, V]): Dictionary to get the first key from

    Returns:
        Optional[K]: The first key from container or None
    """
    try:
        return list(container.keys())[0]
    except IndexError:
        return None


def get_last(container: Dict[K, V]) -> Optional[K]:  # type: ignore
    """ Returns the last key from the dict container

    Args:
        container (Dict[K, V]): Dictionary to get the last key from

    Returns:
        Optional[K]: The last key from container or None
    """
    try:
        listed_dict = list(container.keys())
        return last(listed_dict)
    except IndexError:
        return None


def first(container: List[T]) -> Optional[T]:
    """ Returns the first item from the list container

    Args:
        container (List[T]): List to get the first item from

    Returns:
        Optional[T]: The first item from list or None
    """
    try:
        return container[0]
    except IndexError:
        return None


def last(container: List[T]) -> Optional[T]:
    """ Returns the last item from the list container

    Args:
        container (List[T]): List to get the last item from

    Returns:
        Optional[T]: The last item from list or None
    """
    try:
        last_index = len(container) - 1
        return container[last_index]
    except IndexError:
        return None
