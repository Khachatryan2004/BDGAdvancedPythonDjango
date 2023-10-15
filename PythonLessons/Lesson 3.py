# Homework
# Task 1
# Write a Python program which will remove all zeros from an IP address.
#
# def remove_zero(ip: str) -> str:
#     """
#     Deleting Zero from string ip
#     """
#     return ip.replace("0", "")
#
#
# ip = "216.008.094.196"
# print(remove_zero(ip))

# Task 2
# Given an list of numbers.Find the maximum element inlist.Without use max function.
# def find_max_number(my_list):
#     """
#     Finding maximum number of list
#     """
#     max_number = my_list[0]
#     for i in my_list:
#         if i > max_number:
#             max_number = i
#     return max_number
#
#
# my_list = [1, 8, 3, 6, 55, 93]
# print(find_max_number(my_list))

# Task 3
# Write a Python program that validates passwords based on the following criteria:
# ● The password must be at least 8 characters long.
# ● The password must contain at least one uppercase letter.
# ● The password must contain at least one lowercase letter.
# ● The password must contain at least one digit (0-9).
# ● The password must contain at least one special character (e.g., @, #, $,
# etc.)

# def password_check(password: str) -> str :
#     """
#     Checking if written password strong or not
#     """
#     if len(password) < 8:
#         return "Password is short"
#
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special = False
#
#     special_characters = "!@#$%^&*()_+{}[]:;<>,.?~\\"
#
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in special_characters:
#             has_special = True
#
#     if has_upper and has_lower and has_digit and has_special:
#         return "Good Luck"
#     else:
#         return "Password is wrong"
#
#
# password = input("Password:\t")
#
# print(password_check(password))

# Task 4
# Write a program that takes in a string as input, counts and outputs the number of vowels.
# For example:
# input: test
# output: 1
#
# def vowels(text):
#   '''
#   Counts and outputs the number of vowels.
#   '''
#
#     vowels = "AEIOUaeiou"
#     vowel_count = 0
#
#     for char in text:
#         if char in vowels:
#             vowel_count += 1
#
#     return vowel_count
#
#
# text = input("Write text to count vowels in words:\t")
# print("Number of vowels:", vowels(text))


# Task 5
# Write a function. Create the list which elements are products between two neighbours.
# input : [3, 7, 12, 5, 20, 0] output: [21, 84, 60, 100, 0]
# input : [1, 1, 4, 32, 6] output: [1, 4, 128, 192 ]
#
# def neighbour_product(my_list: list) -> list:
#     '''
#      Elements in list are products between two neighbours
#     '''
#     result = []
#     for i in range(len(my_list) - 1):
#         product = my_list[i] * my_list[i + 1]
#         result.append(product)
#     return result
#
#
# my_list = [3, 7, 5, 0]
# print(my_list)
# print(neighbour_product(my_list))

# Task 6
# Given a sentence with missing words and an array of words. Replace all ‘_’ in a sentence with the words from the array.
# Input “_ we have a _.”
# [“Ashot”, “problem”]
# Output: “Ashot we have a problem.
# def change(my_sentence: str, words: list) -> str:
#     res = []
#     index_words = 0
#     for i in my_sentence:
#         if index_words < len(words) and i == '_':
#             res.append(words[index_words])
#             index_words += 1
#
#         else:
#             res.append(i)
#     return "".join(res)
#
#
# my_sentence = "_ we have a _."
# words = ["Ashot", "problem"]
# print(change(my_sentence, words))

# Task 7
# Given a list of strings. Find the strings with maximum and minimum lengths in array. Print the sum of their lengths.
# Input: [“anymore”, “raven”, “me”, “communicate”]
# Output: 13

# def find_lengths(strings):
#     '''
#     Finding the strings with maximum and minimum lengths, and printing the sum of their lengths
#     '''
#     shortest_word = strings[0]
#     largest_word = strings[0]
#
#     for text in strings:
#         if len(text) < len(shortest_word):
#             shortest_word = text
#
#         elif len(text) > len(largest_word):
#             largest_word = text
#
#     return len(shortest_word) + len(largest_word), shortest_word, largest_word
#
#
# strings = ["anymore", "raven", "me", "communicate"]
# total_length, shortest, largest = find_lengths(strings)
# print("Shortest word:", shortest)
# print("Largest word:", largest)
# print("Sum of lengths:", total_length)

# Task 8
# Given a list of numbers and a number. Find the index of a first element which is equal to that number. If there is
# not such a number, that find the index of the first element which is the closest to it.
# Input Output
# [21, -9, 15, 2116, -71, 33], -71 4
# [ 36, -12, 47, -58, 148, -55, -19, 10], -56 5


# def find_index(my_list, num):
#     for i in range(my_list):
#
#
#
# my_list = [21, -9, 15, 2116, -71, 33]
# num = 4
# print(find_index(my_list))

# Task 9
# Given an dict. Invert it (keys become values and values
# become keys). If there is more than key for that given
# value create an list.Input
# { ‘a’: 1, ‘b’: 2, ‘c’: 2 }
# Output
# { 1: ‘a’, 2: [‘b’, ‘c’] }

# def invert_dict(res):
#     new = {}
#     for key, value in res.items():
#         if value not in new.keys():
#             new[value] = key
#         else:
#             if isinstance(new[value], list):
#                 new[value].append(key)
#             else:
#                 new[value] = [new[value], key]
#     return new
#
#
# res = {'a': 1, 'b': 2, 'c': 2, 'd': 2, 'e': 5, 'z': 5}
# print(res)
# print(invert_dict(res))


# Define a function which can generate a dictionary where the keys are numbers between 1 and N (both included)
# and the values are square of keys. The function should print the dict.Example :
# N = 5
# {1: 1, 2:4, 3:9, 4:16, 5:25}

# def square_of_keys(my_dict):
#     '''
#     Function calculates and stores the squares of keys in the input dictionary
#     '''
#     for i in range(1, 10):
#         my_dict[i] = i ** 2
#
#     return my_dict
#
#
# my_dict = {}
# print(square_of_keys(my_dict))
