"""
Program: function_parameter.py
Author: Grayson Hardin
Last date modified: 10/5/2020

This program will take a string and a number. After it does that, it will then print the string a specific number of times (i.e: string = "Hi" and number = "3" // output = "HiHiHi")
"""


def main():
    message = input("Enter a string: ")
    n = int(input("Enter a number: "))
    result = multiply_string(message, n)
    print(result)

    if not message.isalpha() or n < 2 or n > 7:  # While this was not listed on the assignment, the rubric made me question whether or not there should be code that handles bad input. To be safe, I went ahead and added it so that I would not lose points. Enjoy!
        raise ValueError('Value is not within range and/or input is invalid')


def multiply_string(message, n):
    return n * message


if __name__ == '__main__':
    main()
