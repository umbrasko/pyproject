# -*- coding: utf-8 -*-
import unittest
import doctest
import os.path
import shutil
import re

from tests import input_test_dir
from tests import output_test_dir


class TestUnit(unittest.TestCase):
    # @unittest.skip("temporarily deactivated")
    def test_tex_converter(self):
        example = os.path.join("some", "directory")
        test = True

        self.assertTrue(test, "variable is not True '%s'" %test)
        self.assertEqual(example, "some/directory", "Wrong path")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTex)
    unittest.TextTestRunner(verbosity=1).run(suite)