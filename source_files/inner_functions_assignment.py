"""
Program: inner_functions_assignment.py
Author: Grayson Hardin
Last date modified: 10/4/2020

inner_functions_assignment will take the measurements for a rectangle and a square. It will return the perimeter and area of both objects in a formatted string.
"""


def measurements(list_of_measurements):  # call parameter
    def area(a_list):
        is_rectangle = len(a_list) == 2  # Setting the list default value to 2. While line 12 and 13 could be made into a single, I thought this made the most logical sense
        if is_rectangle:
            return a_list[0] * a_list[1]  # The math then multiplies accordingly
        return a_list[0] * a_list[0]

    def perimeter(a_list):
        is_rectangle = len(a_list) == 2  # Same concept as previously outlined
        if is_rectangle:
            return a_list[0] * 2 + a_list[1] * 2  # Unlike line 14, this has to take into account all four sides
        return a_list[0] * 4

    return f'Perimeter = {perimeter(list_of_measurements)} Area = {area(list_of_measurements)}'  # Formatted string to return appropriate values in custom message


def main():
    rectangle = measurements(list_of_measurements=[3.5, 4])  # Use this to set values for rectangle
    square = measurements(list_of_measurements=[4])  # Use this to set values for square
    print(rectangle)
    print(square)


if __name__ == '__main__':
    main()
