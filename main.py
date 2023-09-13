
# Function computes the sum of list elements
def sum_list(numbers):

    sum = 0

    for value in numbers:
        sum += value 

    return sum 

numbers = [1, 5, 10, 4, 5]
print("Sum of list ---> ", sum_list(numbers))