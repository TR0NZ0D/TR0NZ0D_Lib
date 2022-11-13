import unittest
from tr0nz0d.tools.random_tools import RandomTools


class TestDjangoTools(unittest.TestCase):
    tools = RandomTools()
    testing_array = ["list", 3, 15e+6, None, ("listing", 1.35), False]

    def test_random_picker(self):
        random_item = self.tools.random_pick(self.testing_array)
        self.assertIn(random_item, self.testing_array)


if __name__ == "__main__":
    unittest.main()
