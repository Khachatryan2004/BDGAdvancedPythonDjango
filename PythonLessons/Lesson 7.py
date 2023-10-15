# Homework
# Task 1
# Create a class which given a year, return the century it is in. The first century spans from the year 1 up to
# and including the year 100, the second - from the year 101 up to and including the year 200, etc.
# For year = 1900, the output should be = 19

class YearToCentury:
    def __init__(self, year):
        self.year = year

    def century(self):
        if year % 100 == 0:
            return year // 100

        return year // 100 + 1


year = int(input('Input the year:\t'))
yeartocentury = YearToCentury(year)
print(yeartocentury.century())

# Task 2
# Create a class given the string, check if it is a palindrome.Word should be lowercase and 1 ≤ inputString.length ≤ 105
# Example
# For inputString = "aabaa", the output should be true;
# For inputString = "abac", the output should be false;
# For inputString = "a", the output should be true

class Palindrome:
    def __init__(self, text):
        self.text = text

    def palindrome_check(self):
        return text == text[::-1]

    def palindrome_with_error(self):
        counter = 0

        for i in range(len(text)):
            if text[i] != text[-(i + 1)]:
                counter += 1
                if counter > 2:
                    return False

        return True


text = input('Write text to check if palindrome or not:\t').lower()
palindrome = Palindrome(text)

if palindrome.palindrome_check():
    print(f"Text '{text}' is a palindrome!")
else:
    if palindrome.palindrome_with_error():
        print(f"Text '{text}' is almost a palindrome.")
    else:
        print(f"Text '{text}' is not a palindrome.")


# Task 3
# Create a Class which given an list of integers, find the pair of adjacent elements that has the largest product and
# return that product.
# For inputList = [3, 6, -2, -5, 7, 3],
# the output should be = 21


class Product:
    def __init__(self, my_list):
        self.my_list = my_list

    def product(self):
        enter = int(input('How many numbers or word do you want to add in the list?:\t'))
        for x in range(enter):
            count = int(input(f'{x + 1} generation:\t'))
            my_list.append(count)

        first_number = my_list[0] * my_list[1]
        for i in range(1, len(my_list) - 1):
            if first_number < my_list[i] * my_list[i + 1]:
                first_number = my_list[i] * my_list[i + 1]
        return first_number


my_list = []
p = Product(my_list)
result = p.product()
print(f"The maximum product of list\n {my_list} is: {result}")


# Task 5
#
# Ticket numbers usually consist of an even number of digits.A ticket number is
# considered lucky if the sum of the first half of the digits is equal to the sum of the
# second half.Given a ticket number n, determine if it's lucky or not.
# Example For n= 1230, the output should be
# Lucky(n) = true;
# For n = 239017,
# the output should be Lucky(n) = false


import random


class TicketLucky:
    def __init__(self, number):
        self.number = number

    def process(self):
        num_len = len(str(number))
        half = num_len // 2
        first_half = str(number)[:half]
        second_half = str(number)[half:]
        sum_of_first_half = sum(int(digit) for digit in first_half)
        sum_of_second_half = sum(int(digit) for digit in second_half)
        return sum_of_first_half == sum_of_second_half


number = int(input('Enter the numbers of your ticket:\t'))
ticket_lucky = TicketLucky(number)

prize = [200, 500, 10, 5, 20, 1000]
money = random.choice(prize)

if ticket_lucky.process():
    print(f'Ticket number {number} is lucky! And you win {money}$ ')
else:
    print(f"I'm sorry but the {number} ticket was'nt lucky, next time I'll definitely be lucky")

# Task 6
# Create a class: Some people are standing in a row in a park. There are trees
# between them which cannot be moved. Your task is to rearrange the people by their
# heights in a non-descending order without moving the trees. People can be very tall!
# Example
#  For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
#  sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]

class PeopleSorter:
    def __init__(self, heights):
        self.heights = heights

    def sort_people(self):
        sorted_heights = []
        result = []
        index = 0

        for h in heights:
            if h != -1:
                sorted_heights.append(h)

        sorted_heights.sort()

        for h in heights:
            if h == -1:
                result.append(-1)
            else:
                result.append(sorted_heights[index])
                index += 1

        return result


enter = int(input('Write Heights of people and trees:\t'))
heights = []
for x in range(enter):
    count = int(input(f'{x + 1} generation:\t'))
    heights.append(count)
people_sorter = PeopleSorter(heights)
sorted_heights = people_sorter.sort_people()
print(sorted_heights)


# Task 7
# Several people are standing in a row and need to be divided into two teams. The first
# person goes into team 1, the second goes into team 2, the third goes into team 1
# again, the fourth into team 2, and so on.You are given an array of positive integers -
# the weights of the people. Return an array of two integers, where the first element is
# the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.
# Example For a = [50, 60, 60, 45, 70], the output should be
# alternating Sums(a) = [180, 105].

class AllTeamsWeight:
    def __init__(self, teams_weights):
        self.weights = teams_weights

    def weighs_of_teams(self):
        first_team_weight = 0
        second_team_weight = 0
        team = 1

        for weight in weights:
            if team == 1:
                first_team_weight += weight
                team = 2
            else:
                second_team_weight += weight
                team = 1

        return [first_team_weight, second_team_weight]


enter = int(input('Write total number of players:\t'))
weights = []
for x in range(enter):
    count = int(input(f'{x + 1} player weight:\t'))
    weights.append(count)
all_teams_weight = AllTeamsWeight(weights)
print(all_teams_weight.weighs_of_teams())
