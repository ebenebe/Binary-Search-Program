
# Problem Statement:
# You want to implement a Binary Search algorithm in Python to efficiently search for a target value in a sorted list.

# Question:
# How can I write a Python program that uses the Binary Search algorithm to find a target value in a sorted list?


# welcome message
print('Welcome to Binary Search')
print('===========================')

# Prompt user to enter values
start_num = int(input('enter the start range:'))
end_num = int(input('Enter the end range:'))
target_value = int(input('Enter the number to search for:'))

# Generate and sort random numbers according to user input
user_list = list(range(start_num,end_num + 1))
print(f"\nGenerated List: {user_list}")

# binary search function
def binary_search(sorted_list,target):
    left_value = 0
    right_value = len(sorted_list) - 1

    while left_value <= right_value :
        mid_value = (left_value + right_value) // 2

        if sorted_list[mid_value] == target:
            return mid_value
        elif sorted_list[mid_value] < target:
            left_value = mid_value +1
        else:
            right_value = mid_value -1
    return -1

# call Binary search function
result = binary_search(user_list,target_value)
if result != -1:
    print(f'Target found at index {result}')
else:
    print('Target not found')



