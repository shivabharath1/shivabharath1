import math

# Function to check if a number is a strong number
def is_strong_number(num):
    sum_factorials = 0
    for digit in str(num):
        sum_factorials += math.factorial(int(digit))
    return sum_factorials == num

# Function to print strong numbers between 1 to 5000
def strong_numbers_in_range(start, end):
    for num in range(start, end + 1):
        if is_strong_number(num):
            print(num)

# Printing strong numbers between 1 and 5000
strong_numbers_in_range(1, 5000)