import unittest
import Tests

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
