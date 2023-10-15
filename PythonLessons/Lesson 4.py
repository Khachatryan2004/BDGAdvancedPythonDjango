# Linear Search algorithm
# def linery_search(my_list, n, x):
#     for i in range(n):
#         if my_list[i] == x:
#             return i
#     return -1
#
#
# my_list = [2, 3, 4, 10, 40, 21]
# x = 21
# n = len(my_list)
# result = linery_search(my_list, n, x)
# if result == -1:
#     print('Element is not present in list')
# else:
#     print('Element is present at index', result)
#

# Binery Search Algorithm
# def binery_search(my_list, search, start, stop):
#     if start > stop:
#         return False
#     else:
#         mid = (start + stop) // 2
#         if search == my_list[mid]:
#             return mid
#         elif search < my_list[mid]:
#             return binery_search(my_list, search, start, mid - 1)
#         else:
#             return binery_search(my_list, search, mid + 1, stop)
#
#
# search = 156
# start = 0
# my_list = [1, 12, 14, 18, 27, 34, 56, 89, 123, 156198, 300, 900, 990, 1020]
# stop = len(my_list)
#
# result = binery_search(my_list, search, start, stop)
#
# if search == False:
#     print('Item', search, 'Not Found')
# else:
#     print('Item', search, 'Found at index :', result)

# Bubble Sort Algorithm

# old_list = [10, 75, 43, 15, 25, -4, 27]
#
#
# def bubble_sort(my_list):
#     last_item = len(my_list) - 1
#
#     for i in range(last_item):
#         for j in range(last_item - i):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
#
#     return my_list
#
#
# print('Old List', old_list)
# new_list = bubble_sort(old_list).copy()
# print('New List:', new_list)

# Imagine you and the computer are playing tennis. write a program where you have a sheet where victory points are
# kept and you need to figure out who is the winner.A set is won by the first side to win 6 games. You should to show
# the result of the match. If game win you in list add “a” if pc “b”.

import random

#
#
# import random
#
#
# def tennis_game():
#     '''
#     Simulates a tennis game and determines the winner based on the first player to win 6 games
#     '''
#     result = []
#     you_wins = 0
#     computer_wins = 0
#     victory_win = 6
#
#     while True:
#         winner = random.choice(['You', 'Computer'])
#         result.append(winner)
#
#         if winner == 'You':
#             you_wins += 1
#
#         elif winner == 'Computer':
#             computer_wins += 1
#
#         if you_wins == victory_win - 1 and computer_wins == victory_win - 1:
#             victory_win += 1
#
#         if you_wins == victory_win:
#             print("You win!, Congratulations")
#             break
#
#         elif computer_wins == victory_win:
#             print('Computer win!, You will win next time')
#             break
#
#     print("Result of the game: ", result)
#
#
# tennis_game()

# Given three numbers a, b (a ≤ b) and step. Create an list of evenly spaced elements starting from a to b spaced by
# step you have 3 argument: Input Output
# 1 5 1 [1, 2, 3, 4, 5]
# 10 100 20 [10, 30, 50, 70, 90]

# def steps(start, stop, step):

#     l = []
#     for i in range(start, stop, step):
#         l.append(i)
#     return l
#
#
# start = int(input("Start number:\t"))
# stop = int(input("Stop number:\t"))
# step = int(input("Steps:\t"))
# print(steps(start, stop, step))


