# This comment was added to fulfill part 10 of the
# homework assignment



# Function computes the sum of list elements
def sum_list(numbers):

    sum = 0

    for value in numbers:
        sum += value 

    return sum 

# Computes the product of list elements
def multiply_list(numbers):

    if len(numbers) > 0:
        product = 1
    else:
        product = 0

    for value in numbers:
        product *= value
    
    return product

# Reverses a list
def reverse_list(numbers):

    reversed_list = []
    i = len(numbers) - 1

    while i >= 0:
        reversed_list.append(numbers[i])
        i -= 1
    
    return reversed_list

# Main function
if __name__ == "__main__":

    numbers = [1, 5, 10, 4, 5]
    print("Sum of list ---> ", sum_list(numbers))
    print("Product of list ---> ", multiply_list(numbers))
    print("Reversed list -----> ", reverse_list(numbers))