# Homework
# Task 1
# Write a python class to find max, min num and sum
# don’t use max sum and min function

# class ForList:
#     def __init__(self, my_list):
#         self.my_list = my_list
#
#     def max_number(self):
#
#         max_num = my_list[0]
#         for num in self.my_list:
#             if num > max_num:
#                 max_num = num
#         return max_num
#
#     def min_number(self):
#         min_num = my_list[0]
#         for num in self.my_list:
#             if num < min_num:
#                 min_num = num
#         return min_num
#
#     def sum_of_list(self):
#         summary = 0
#         for num in self.my_list:
#             summary += num
#         return summary
#
#
# my_list = [5, 8, 2, 5, 9, 13, 26, 74, 30]
# result = ForList(my_list)
# print(" Max number of the list is", result.max_number(), '\n', "Min number of the list is", result.min_number(), '\n',
#       "And summary of the list is", result.sum_of_list())


# Task 2
# Write a python class to find two highest values in your dict:
#
#
# class DictionaryHighestValues:
#     def __init__(self, my_dict):
#         self.my_dict = my_dict
#
#     def find_highest_values(self):
#
#         highest_value = 0
#         second_highest_value = 0
#
#         for key, value in self.my_dict.items():
#             if value > highest_value:
#                 second_highest_value = highest_value
#                 highest_value = value
#             elif value > second_highest_value:
#                 second_highest_value = value
#         return highest_value, second_highest_value
#
#
# my_dict = {'a': 10, 'b': 25, 'c': 5, 'd': 30}
# result = DictionaryHighestValues(my_dict)
# print(result.find_highest_values())


# Task 3
# Write a python class where your child class takes all methods in parent class and print them.
#
#
# class Parent:
#     def __init__(self, name, age, gender, country):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.country = country
#
#     def show(self):
#         print(
#             f'Hello, I am {self.name}, I am {self.age} years old. My gender is {self.gender} and I am from {self.country}')
#
#
# class Child(Parent):
#     def __init__(self, name, age, gender, country):
#         super().__init__(name, age, gender, country)
#
#
# child = Child('Alex', 16, 'male', 'Armenia')
# child.show()

# Task 4
# Write a Python class named Rectangle constructed bya length and width and a method which will compute the
# area of a rectangle.
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#
# rectangle_width_and_length = Rectangle(5, 8)
# print('Area of the Rectangle is', rectangle_width_and_length.area())

# Task 5
# Write a python class where we use polymorphism:
#
# class Place:
#     def country(self):
#         pass
#
#
# class Yerevan(Place):
#     def country(self):
#         return 'Yerevan'
#
#
# class Paris(Place):
#     def country(self):
#         return 'Paris'
#
#
# yerevan = Yerevan().country()
# paris = Paris().country()
# print(yerevan, paris)
#
#

# Task 6
# Create a class Change:You have 3 methods in your class:
# Usd --- Eur
# Usd --- Amd
# Usd --- Ru

class CurrencyConversion:
    def usd_eur(self, amount_usd):
        return amount_usd * 0.94

    def usd_amd(self, amount_usd):
        return amount_usd * 397.11

    def usd_rub(self, amount_usd):
        return amount_usd * 98


change = CurrencyConversion()

amount_usd = float(input('Amount USD:\t'))
eur_amount = change.usd_eur(amount_usd)
print(f"{amount_usd} USD is {eur_amount} EUR")

usd_amount = float(input('Amount USD:\t'))
amd_amount = change.usd_amd(amount_usd)
print(f"{usd_amount} USD is {amd_amount} AMD")

usd_amount = float(input('Amount USD:\t'))
ru_amount = change.usd_rub(amount_usd)
print(f"{usd_amount} USD is {ru_amount} RUB")
