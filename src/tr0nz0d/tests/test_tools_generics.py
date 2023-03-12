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

Created by: Gabriel Menezes de Antonio (TR0NZ0D)
"""
import unittest

from tr0nz0d.tools.generics import first, get_first, get_last, last


class TestList(unittest.TestCase):
    """Test case for lists"""
    testing_list = [1, 7, 4, 3, 5]

    def test_list_first(self):
        """Test case for first item in list"""
        self.assertEqual(first(container=self.testing_list), 1)

    def test_list_last(self):
        """Test case for last item in list"""
        self.assertEqual(last(container=self.testing_list), 5)


class TestDict(unittest.TestCase):
    """Test case for dicts"""
    testing_dict = {"1": 1, 2: 2, "3": [], 4: {}}

    def test_dict_first(self):
        """Test case for first item in dict"""
        self.assertEqual(get_first(container=self.testing_dict), "1")

    def test_dict_last(self):
        """Test case for last item in dict"""
        self.assertEqual(get_last(container=self.testing_dict), 4)


if __name__ == "__main__":
    unittest.main()
