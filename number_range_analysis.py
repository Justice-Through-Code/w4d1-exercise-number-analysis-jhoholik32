#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION
# This program is designated to calculate the sum of numbers in a specified range
# Ill be doing this by using the range and sum function.
# then ill return the function
def calculate_sum(start, end):
    
    """
    Calculate the sum of numbers within the specified range.
    
    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # this range function is gathering the range of numbers within the specified index
    # I added plus on because the end value to be included othewise it wouldnt be
    x = 0
    # here is used the sum function to calculate the sum of the designated range within the to calculate the sum of the specified range
    for num in range(start, end + 1):
        x += num
    # I then store the sum using the return function
    return x
    
    
    # TODO: Return the calculated sum.
# calculate_sum(1,5)

def find_smallest_number(start, end):
    """
    Find the smallest number within the specified range.
    # list = range(int(start, end))
    #     print(min(list))
    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
# Initialize the smallest number with the first number in the range
    smallest_number = start
# next i am going Iterate over the numbers in the range
    for num in range(start, end):
        if num < smallest_number:
            smallest_number = num
    # TODO: Return the found smallest number.
    # then i return the smallest
    return smallest_number

def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    #  For the largest number I Initialize the largest number
    largest_number = end
    # then i iterate over the numbers in the range
    for number in range(start, end):
        if number > largest_number:
            largest_number = number

    # TODO: Return the found largest number.
    # then Return the largest number
    return largest_number

def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # intialize variable
    even_num = 0
    # then run logic to find the math using % opperator
    for num in range(start, end + 1):
        if ((num // 2) * 2 == num):
            even_num += 1
    return even_num
    # TODO: Return the count of even numbers.

def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    #  intilize variable
    odd_num = 0
    # then run the logic to count the numbers not devisible by 2 making them odd
    for num in  range(start, end + 1):
        if ((num // 2) * 2 != num):
            odd_num += 1

    # TODO: Return the count of odd numbers.
    # then I return the results of the logic
    return odd_num