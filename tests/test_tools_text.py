import unittest
from tr0nz0d.tools.text import TextFormat


class TestTextFormatter(unittest.TestCase):
    formatter = TextFormat()

    def test_line_print_formatter(self):
        print_result = self.formatter.line_print("", "", "", "", "", "", "")
        self.assertEqual(print_result, None)

    def test_text_print_formatter(self):
        print_result = self.formatter.text_print("", "", "", "", "", "", "")
        self.assertEqual(print_result, None)


if __name__ == "__main__":
    unittest.main()
