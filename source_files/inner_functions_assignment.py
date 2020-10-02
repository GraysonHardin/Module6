"""
Grayson Hardin
Program: inner_functions_assignment.py
Date Last Modified: 10/2/2020

"""


def measurements(list_of_measurements):
    def area(a_list):
        is_rectangle = len(a_list) == 2
        if is_rectangle:
            return a_list[0] * a_list[1]

    def perimeter(a_list):
        is_rectangle = len(a_list) == 2
        if is_rectangle:
            return a_list[0] * 2 + a_list[1] * 2

    return f'Perimeter = {perimeter(list_of_measurements)} Area = {area(list_of_measurements)}'


def main():
    rectangle = measurements(list_of_measurements=[3.5, 4])
    print(rectangle)


if __name__ == '__main__':
    main()
