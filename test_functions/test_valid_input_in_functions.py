import unittest
from more_functions.validate_input_in_functions import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):  # Ultimately, this is what I want to return: a formatted message with the test_name and a proper integer value
        test_name = 'Python Exam 101'
        expected = f'{test_name}: {0}'

        actual = score_input(test_name)
        self.assertEqual(expected, actual)

    def test_score_input_test_score_valid(self):  # This test provides a good example of what a proper scenario should be
        test_name = 'Python Exam 101'
        test_score = 90

        expected = f'{test_name}: {test_score}'
        actual = score_input(test_name, test_score)

        self.assertEqual(expected, actual)

    def test_score_input_test_score_below_range(self):  # This test provides a scenario for if the test_score is under the range
        with self.assertRaises(ValueError):
            test_name = 'Python Exam 101'
            test_score = -1

            score_input(test_name, test_score)

    def test_score_input_test_score_above_range(self):  # This test provides a scenario for if the test_score is above the range
        with self.assertRaises(ValueError) as err:
            test_name = 'Python Exam 101'
            test_score = 101

            score_input(test_name, test_score)
        self.assertTrue('Invalid test score, try again!' in str(err.exception))

    def test_score_input_non_numeric(self):  # Notice that for test_score I have added a section to validate whether the value is a string or integer
        with self.assertRaises(ValueError) as err:
            test_name = 'Python Exam 101'
            test_score = 'Invalid input value'

            score_input(test_name, test_score)
        self.assertTrue('Invalid test score, try again!' in str(err.exception))

    def test_score_input_invalid_message(self):  # Finally, we include all arguments and validate invalid_message
        with self.assertRaises(ValueError) as err:
            test_name = 'Python Exam 101'
            test_score = -50
            invalid_message = 'Custom invalid error message'

            score_input(test_name, test_score, invalid_message)
        self.assertTrue(invalid_message in str(err.exception))


if __name__ == '__main__':
    unittest.main()
