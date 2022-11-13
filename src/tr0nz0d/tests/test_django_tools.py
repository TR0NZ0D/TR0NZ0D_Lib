import unittest
from tr0nz0d.django_tools.tools import DjangoTools


class _MockedRequest:
    META = {
        'HTTP_X_FORWARDED_FOR': "192.168.0.1,?,?,?, ?, ??",
        'REMOTE_ADDR': "192.168.0.1"
    }


class TestDjangoTools(unittest.TestCase):
    tools = DjangoTools()
    mocked_request = _MockedRequest()
    mocked_ip_address = "192.168.0.1"

    def test_visitor_ip_address(self):
        visitor_ip = self.tools.visitor_ip_address(self.mocked_request)
        self.assertEqual(visitor_ip, self.mocked_ip_address)


if __name__ == "__main__":
    unittest.main()
