import unittest

class MyUnitTests(unittest.TestCase):
    def test_some_functionality(self):
        print('testing some functionality')
        # do an assert to pass or fail a test
        result = True
        self.assertEqual(True, result)



if __name__ == '__main__':
    unittest.main()
    