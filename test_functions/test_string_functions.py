import unittest
from more_functions.string_functions import multiple_string


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        user_name = 'Grayson'
        expected = user_name * 3

        actual = multiple_string(user_name * 3)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
