import unittest
from Tests import json_tests
import sys
import os


def run_tests():
    suite = unittest.TestLoader().loadTestsFromModule(json_tests)
    sys.stdout = open(os.devnull, 'w')
    unittest.TextTestRunner(verbosity=2).run(suite)
    sys.stdout = sys.__stdout__
