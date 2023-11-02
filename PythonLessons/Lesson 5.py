# Task 1
# Write a recursive function to determine whether all digits of the number are odd or not.
# Input Output
# 4211133 False
# 7791 True
# 5 True
#
# def all_digits_odd(number):
#     pass
#
#
# # Test the function
# number = int(input('Input number:\t'))


# Task 2
# Write a python function all even number in 10.000 use threading and print time
#
# import threading
# import time
#
#
# def even(number):
#     return number % 2 == 0
#
#
# def odd(number):
#     return number % 3 == 0
#
#
# def even_odd(start_number, end_number):
#     for i in range(start_number, end_number + 1):
#         if even(i):
#             with open('even_numbers.txt', 'a') as evenf:
#                 evenf.write(str(i) + '\n')
#         elif odd(i):
#             with open('odd_numbers.txt', 'a') as oddf:
#                 oddf.write(str(i) + '\n')
#
#
# start_number = int(input('Start number: '))
# end_number = int(input('End number: '))
#
# start_time = time.time()
#
# even_thread = threading.Thread(target=even_odd, args=(start_number, end_number // 2))
# odd_thread = threading.Thread(target=even_odd, args=(start_number // 2, end_number + 1))
# even_thread.start()
# odd_thread.start()
# even_thread.join()
# odd_thread.join()
#
# end_time = time.time()
#
# print(f"Time taken: {end_time - start_time:.2f} seconds")

# Task 3
# Given N number. Write a recursive function that should print from 1 to N numbers.
# Input Output
# 5     1, 2, 3, 4, 5

# def to_n(num):
#     if num >= 1:
#         to_n(num - 1)
#         print(num, end=', ')
#
#
# number = int(input('Number:\t'))
# to_n(number)

# Task 4
# Write a python program to find the longest word from the file content.Need to use <try-except> block in the file
# reading process and print time. example:
# 1. try:
# 2. with open("filename.txt") as file:
# 3. some code
# 4. except:
# 5. do something
# 6. Function call: find_long_word("filename.txt")
# 7. Function output: "LongestWord
#
# import time
#
#
# def longest_word_in_file(file_name: str) -> str:
#     '''
#     Finds and returns the longest word in a text file.
#
#     return: The longest word found in the file.
#     '''
#     try:
#         start_time = time.time()
#         with open(file_name, 'r') as longf:
#             words = longf.read().split()
#             longest_word = ''
#             for word in words:
#                 if len(word) > len(longest_word):
#                     longest_word = word
#         end_time = time.time()
#         print(f'Time taken: {end_time - start_time:.3f}')
#
#         return longest_word
#     except FileNotFoundError:
#         return 'No such file'
#
#
# file_name = 'longest_word_lesson5'
# result = longest_word_in_file(file_name)
# if result == 'No such file':
#     print(f"Error! No such file like: {file_name}:")
# else:
#     print(f'Longest Word in file:{file_name}: is - {result}')
