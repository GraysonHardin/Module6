import unittest
from more_functions.string_functions import multiple_string


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        expected = 'BobBobBob'

        actual = multiple_string(message='Bob', n=3)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
