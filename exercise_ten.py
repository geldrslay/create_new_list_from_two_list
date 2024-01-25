# Create a new list from two list using the following condition:
# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# Provide two given list.
number_list1 = [10, 20, 25, 30, 35]
number_list2 = [40, 45, 60, 75, 90]

# Defining function 
def create_new_list (number_list1, number_list2):
    result_list = []
    # Reiterate the first list. 
    for number in number_list1:
        # Check if numbers on the list are odd.
        if number %2 != 0:
            result_list.append(number)
