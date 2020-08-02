import unittest
import os
from Week2.run import get_files


class TestRun(unittest.TestCase):

    def test_path(self):
        self.assertRaises(OSError, get_files("/data/feedback"))

    def test_get_files(self):
        self.assertGreater(len(get_files("/data/feedback")), 0)


if __name__ == '__main__':
    unittest.main()
