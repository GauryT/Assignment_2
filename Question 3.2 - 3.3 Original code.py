
def process_numbers(numbers=None):
    """
    Function to process a list of numbers.

    :param numbers: A list of numbers to process. If None, the default list is used.
    :return: The processed list of numbers.
    """
    # Define the global variable that will be used in the function
    global glocal_variable

    # Define the local variable
    local_variable = 5

    # Define default list of numbers
    default_numbers = [1, 2, 3, 4, 5]

    # If the numbers parameter is None, then use the default list
    if numbers is None:
        numbers = default_numbers
    else:
        # Convert the set to a list
        numbers = list(numbers)

    # Loop while the local variable is greater than 0
    while local_variable > 0:
        # If the local variable is even
        if local_variable % 2 == 0:
            # Remove the element at the index of the local variable minus 1
            numbers.pop(local_variable - 1)
        # Decrement the local variable
        local_variable -= 1

    # Return the processed list of numbers
    return numbers

# Define a set of numbers
my_set = {1, 2, 3, 4, 5}

# Call the process_numbers function with the my_set set
result = process_numbers(numbers=my_set)