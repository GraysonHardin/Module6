"""
Grayson Hardin
Program: validate_input_in_function.py
Date last modified: 9/30/2020

This program will ask for two user inputs: a test name and a test score. The inputs have conditions and limits. If the input is not within the limits (range) it will loop until met. Once it has been met, it will print the two values in a formatted message.

The first parameter is test_name: It will take an input from the user and does not require validation.
The second parameter is test_score: The default value has been assigned to 0 and allows the user to input their score. If the user chooses a number less than 0 or a value greater than 100, it will notify the user of invalid input and ask again.
The third parameter is invalid_message: The default value has been assigned to, "Invalid test score, try again!" That message is given every time a invalid value is inputted (i.e: -1 or 101).
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):  # Parameter values given.
    if isinstance(test_score, str) or test_score < 0 or test_score > 100:  # Here we define the condition and limitations of the error message.
        raise ValueError(invalid_message)

    return f'{test_name}: {test_score}'  # Returns the test_name and test_score in a formatted string


def main():
    try:
        user_test_name_input = input('Enter a test name: ')  # Gain input for test name
        user_test_score_input = int(input('Enter a test score: '))  # Gain input for test score
        results = score_input(user_test_name_input, user_test_score_input)  # Calculation of the two previous values
        print(results)
    except ValueError as err:
        print('Error: ', err)  # If an error occurs, it will print "Error" along with the specific message.
        main()


if __name__ == '__main__':
    main()
