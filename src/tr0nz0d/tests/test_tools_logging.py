import unittest
from tr0nz0d.tools.logging import Log, LoggingLevels


class TestLogging(unittest.TestCase):
    logging_level = LoggingLevels.DEBUG
    log = Log(logging_level)

    def test_logging(self):
        logging_return = self.log.debug("Log completed")
        self.assertEqual(logging_return, None)


if __name__ == "__main__":
    unittest.main()
