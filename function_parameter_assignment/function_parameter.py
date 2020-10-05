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


def multiply_string(message, n):
    return n * message


if __name__ == '__main__':
    main()
