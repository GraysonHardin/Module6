"""
Program: basic_function.py
Author: Grayson Hardin
Last date modified: 10/5/2020


The program will take multiple inputs and store it within a list if it is within the parameters (1-100).
I have ran this program many times and have provided my documentation down below.

"""


def hourly_employee_input():
    name = input("Enter name: ")  # Gain name input
    hours_worked = int(input("Enter hours worked: "))  # Gain hours input
    salary = float(input("Enter salary: "))  # Gain salary input

    if not name.isalpha() or hours_worked < 0 or salary < 0:  # This will raise an error if the name does not equal a string, if hours is less than 0 and if salary is less than 0.
        raise ValueError('Value is negative and/or not valid')  # Programmer can add custom message here.

    print(f'Name is {name}:  hours: {hours_worked} salary is ${salary} an hour.')  # formatted string


def main():
    try:
        hourly_employee_input()
    except ValueError as err:
        print('Invalid input: ', err)  # prints error message


if __name__ == '__main__':
    main()
