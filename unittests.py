import unittest

class TestCases(unittest.TestCase):
    def test_something(self):
        self.assertEqual('method', 'value')
        self.assertTrue('soemthing'.isupper())

if __name__ == '__main__':
    unittest.main()