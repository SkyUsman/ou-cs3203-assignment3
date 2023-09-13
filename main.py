
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

# Main function
if __name__ == "__main__":

    numbers = [1, 5, 10, 4, 5]
    print("Sum of list ---> ", sum_list(numbers))
    print("Product of list ---> ", multiply_list(numbers))