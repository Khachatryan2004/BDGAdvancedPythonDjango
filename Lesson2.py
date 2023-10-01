# Homework


# # Task 1
# Create a python program which will say which number used more. my_list = [1,3,4,5,1,2,3,1] output: number 1 - 3 times
#
# my_list = [1, 2, 3, 9, 5, 9, 2, 7, 4, 0, 2, 1]
# number_count = {}
# for number in my_list:
#     if number in number_count:
#         number_count[number] += 1
#     else:
#         number_count[number] = 1
#
# for number in number_count:
#     count = number_count[number]
#     print(f"Number:{number} - {count} Times")

# Task 2
#  Write a Python program to sum all the items in a list. use list comprehension

# my_list = [sum(i) for i in range(10)]  # chexav es dzevov
# print(my_list)
#
# s = sum([x for x in (range(10))])  # senc exav
# print(s)

# Task 3
# Write a Python program to get the largest text from a list.
#
# my_list = ["Ani", "Ashot", "Diana", "Hasmik", "Aramayis"]
# largest_text = []
# for text in my_list:
#     if len(text) > len(largest_text):
#         largest_text = text
#
# print(largest_text)

# Task 4
# Write a Python program that have two lists and returns True if they have at least one common member.
#
# def two_lists(l1, l2: str) -> bool:
#     for word1 in l1:
#         for word2 in l2:
#             if word1 == word2:
#                 return True
#     return False
#
#
# l1 = ['apple', 'kiwi', 'banana', 'dog']
# l2 = ['cat', 'dog', 'sheet', 'eye']
#
# print(two_lists(l1, l2))


# Task 5
# Write a Python program to Sort Words in Alphabetic Order
# Chstacvec

# Task 6
# Write a Python program that creates a generator function that generates all prime numbers between two given numbers.
# def is_prime(number: int) -> str:
#     for i in range(2, number):
#         if number % i == 0:
#             return "Number is not prime"
#     return "Number is prime"
#
#
# def prime_numbers(start, end: int) -> int:
#     for number in range(start, end + 1):
#         if is_prime(number):
#             yield number
#
#
# start = int(input("Input the start number:\t"))
# end = int(input("Input the end number:\t"))
# print(prime_numbers(start))
# print(prime_numbers(end))
# print(f"Prime numbers between {start} and {end}:".format(start, end))
# for prime in prime_numbers(start, end):
#     print(prime)
# Chstacvec


# Task 7
# Create python program which will check if your password is strong or no. if Len
# your password is great than 8 and if your password have 2 numbers and 2 of the
# following special characters ('!', '@', '#', '$', '%', '&', '*')
# Sample Input: Python@$World11
# Sample Output: Strong
#
# def password_check(password: str) -> bool:
#     """
#     Checking if written password strong or not
#     """
#     characters = '!', '@', '#', '$', '%', '&', '*'
#     digit_count = 0
#     characters_count = 0
#     if len(password) < 8:
#         return False
#
#     for char in password:
#         if char.isdigit():
#             digit_count += 1
#         elif char in characters:
#             characters_count += 1
#
#     if digit_count >= 2 and characters_count >= 2:
#         return True
#     else:
#         return False
#
#
# password = input("Password:\t")
#
# if password_check(password):
#     print("Password is strong")
# else:
#     print("Password is not strong")

# Task 8
# Create python program where you want to find id in link if link have id print id.
# Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU
# Sample Output: RRW2aUSw5vU
#
# def find_youtube_id(link):
#     """
#     Finding youtube link id and extract it
#     """
#     for i in link:
#         if '=' in i:
#             return link[link.index('=') + 1:]
#
#
# link = input("Input Link:\t")
# print(find_youtube_id(link))

# Task 9
# Write a Python program that implements a decorator to validate function arguments based on a given condition.
#
# def multiply(func):
#     def process(number):
#         x = 10
#         result = func(number)
#         return result * x
#
#     return process
#
#
# @multiply
# def num(number):
#     return number
#
#
# result = num(10)
# print(result)
