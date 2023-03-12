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

from tr0nz0d.django_tools.tools import DjangoTools


class _MockedRequest:
    """Mocked test request"""
    META = {
        'HTTP_X_FORWARDED_FOR': "192.168.0.1,?,?,?, ?, ??",
        'REMOTE_ADDR': "192.168.0.1"
    }


class TestDjangoTools(unittest.TestCase):
    """Test case for django tools"""
    tools = DjangoTools()
    mocked_request = _MockedRequest()
    mocked_ip_address = "192.168.0.1"

    def test_visitor_ip_address(self):
        """Test getting visitor's ip address"""
        visitor_ip = self.tools.visitor_ip_address(self.mocked_request)
        self.assertEqual(visitor_ip, self.mocked_ip_address)


if __name__ == "__main__":
    unittest.main()
