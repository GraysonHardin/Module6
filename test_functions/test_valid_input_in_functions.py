import unittest
from more_functions.validate_input_in_functions import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        test_name = 'Python Exam 101'
        expected = f'{test_name}: {0}'

        actual = score_input(test_name)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
