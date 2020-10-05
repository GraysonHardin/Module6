"""
Program: basic_function.py
Author: Grayson Hardin
Last date modified: 10/5/2020


The program will take multiple inputs and store it within a list if it is within the parameters (1-100).
I have ran this program many times and have provided my documentation down below.

"""


def hourly_employee_input():
    name = input("Enter name: ")  # Line 14 (as well as 15, 16) gain input
    hours_worked = int(input("Enter hours worked: "))
    hourly_pay_rate = float(input("Enter hourly rate: "))

    if not name.isalpha() or hours_worked < 0 or hourly_pay_rate < 0:  # Raises an error if the conditions are not met
        raise ValueError('Value is negative and/or not valid')

    pay_summary = weekly_pay(hours_worked, hourly_pay_rate)

    return name, pay_summary


def weekly_pay(hours_worked, hourly_pay_rate):
    weekly_salary = hours_worked * hourly_pay_rate  # This will calculate the weekly pay
    return weekly_salary


def main():
    try:
        name, summary = hourly_employee_input()
        print(f'The name is: {name} and the weekly pay is: ${summary}')  # Formatted string
    except ValueError as err:
        print('Invalid input: ', err)


if __name__ == '__main__':
    main()
