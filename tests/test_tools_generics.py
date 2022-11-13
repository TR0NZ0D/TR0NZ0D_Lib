import unittest
from tr0nz0d.tools.generics import first, last, get_first, get_last


class TestList(unittest.TestCase):
    testing_list = [1, 7, 4, 3, 5]

    def test_list_first(self):
        self.assertEqual(first(container=self.testing_list), 1)

    def test_list_last(self):
        self.assertEqual(last(container=self.testing_list), 5)


class TestDict(unittest.TestCase):
    testing_dict = {"1": 1, 2: 2, "3": [], 4: {}}

    def test_dict_first(self):
        self.assertEqual(get_first(container=self.testing_dict), "1")

    def test_dict_last(self):
        self.assertEqual(get_last(container=self.testing_dict), 4)


if __name__ == "__main__":
    unittest.main()
