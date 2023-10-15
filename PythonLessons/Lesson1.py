# Homework

# Task 1
#
# def basics_of_lambda():
#     """
#      Multiplying any number by 10
#     """
#     return lambda x: x * 10
#
#
# multiply = basics_of_lambda()
#
# number = int(input("Input number:\t"))
# result = multiply(number)
# print(result)


# # Task 2
#
# def using_map(x):
#     """
#     Doubling number in given list
#     """
#     return x * 2
#
#
# print(list(map(using_map, range(1, 10))))


# # Task 3
#
# def using_filter(x):
#     """
#     Extracting all the even numbers
#     """
#     return x % 2 == 0
#
#
# numbers = list(range(1, 10))
# even_numbers = list(filter(using_filter, numbers))
# print(numbers)
# print(even_numbers)


from functools import reduce


# Task 4
# def using_reduce(x, y):
#     """
#     Finding the product of all numbers in a given list
#     """
#     return x * y
#
#
# numbers = list(range(1, 6))
# print(numbers)
# result = reduce(using_reduce, numbers)
# print(result)

# Task 5
# def is_prime(x):
#     '''
#     Determining if a number is prime
#     '''

# # Task 6
# def even(x):
#     return x % 2 == 0
#
#
# def square(x):
#     return x ** 2
#
#
# numbers = list(range(1, 10))
# print(numbers)
# even_numbers = list(filter(even, numbers))
# print(even_numbers)
# even_squared_numbers = list(map(square, even_numbers))
# print(even_squared_numbers)


# Task 7

# def calculator(num1, num2, operator):
#     """
#     Calculator
#     """
#     if operator == '+':
#         return f"{num1} {operator} {num2} = {num1 + num2}"
#
#     elif operator == '-':
#         return f"{num1} {operator} {num2} = {num1 - num2}"
#
#     elif operator == '*':
#         return f"{num1} {operator} {num2} = {num1 * num2}"
#     elif operator == '/':
#         if num2 == 0:
#             return 'Cant divide by 0'
#         return f"{num1} {operator} {num2} = {num1 / num2}"
#     else:
#         return 'Invalid Operator'
#
#
# num1 = float(input("First number:\t"))
# num2 = float(input("Second number:\t"))
# operator = input("Operator: + - * / \t")
# print(calculator(num1, num2, operator))

# Task 8

# def max_number(a, b):
#     '''
#     Finding max number
#     '''
#     if a > b:
#         return a
#     else:
#         return b
#
#
# num1 = float(input('First number:\t'))
# num2 = float(input('Second number:\t'))
# result = max_number(num1, num2)
# print(f'The maximum number is {result}')

# Task 9

# def sum_list_numbers():
#     """
#     Sum all the numbers in a list
#     """
#     for number in numbers_list:
#         return sum(numbers_list)
#
#
# numbers_list = [1, 2, 3, 4, 5]
# print(numbers_list)
# print(sum_list_numbers())

# Task 10

# def multiply_list_numbers(numbers):
#     """
#     Multiplying all the numbers in a given list
#     """
#     result = 1
#     for number in numbers:
#         result *= number
#     return result
#
#
# numbers_list = [1, 2, 3, 4, 5]
# print(numbers_list)
# result = multiply_list_numbers(numbers_list)
# print(result)

# Task 11

def passengers_ages():
    """
    Checking if all passengers is 16+
    """
    ages = []
    i = 1
    while i <= 3:
        age = int(input(f"Enter the age of passenger {i}:\t"))
        ages.append(age)
        if age < 16:
            print("Too young!")
            break
        i += 1
    if len(ages) == 3:
        print("Get Ready!")


passengers_ages()
