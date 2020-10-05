"""
Program: string_functions.py
Author: Grayson Hardin
Last date modified: 10/5/2020

This will take a string, a number, and multiple them together. Testing was included as well.
"""


def multiple_string(message, n):
    calculation = message * n
    return calculation


def main():
    message = input("Enter a string: ")
    n = int(input("Enter a number: "))
    calculation = multiple_string(message, n)
    print(calculation)


if __name__ == '__main__':
    main()
