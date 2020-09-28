"""
Program: basic_function.py
Author: Grayson Hardin
Last date modified: 9/28/2020


The program will take multiple inputs and store it within a list if it is within the parameters (1-100).
I have ran this program many times and have provided my documentation down below.

"""
"""
def hourly_employee_input():
    user_string_input = input("Enter string value: ")
    user_integer_input = int(input("Enter integer value: "))
    user_float_input = float(input("Enter float value: "))
    print(user_string_input, user_integer_input, user_float_input)
"""


def hourly_employee_input():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))

    if not name.isalpha() or age < 0 or salary < 0:
        raise ValueError('Value is negative and/or not valid')

    print(f'Name is {name}:  age: {age} salary is ${salary} an hour')


def main():
    try:
        hourly_employee_input()
    except ValueError as err:
        print('Invalid input: ', err)


if __name__ == '__main__':
    main()
