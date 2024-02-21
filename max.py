def find_max(*args):
    
    if not args:
        return None  # Return None if no arguments are provided
    
    max_number = args[0]  # Initialize max_number with the first argument
    for number in args:
        if number > max_number:
            max_number = number
    return max_number

# Input tuple of numbers from the user
user_input = input("Enter a tuple of numbers separated by commas: ")

# Split the input string at commas and convert each part into an integer
numbers_list = [int(num) for num in user_input.split(',') if num.strip().isdigit()]

# Convert the list of numbers into a tuple
numbers_tuple = tuple(numbers_list)

# Example usage:
maximum = find_max(*numbers_tuple)
if maximum is not None:
    print("The maximum number among the given tuple values is:", maximum)
else:
    print("No valid tuple values provided.")
def find_min(*args):
    
    if not args:
        return None  # Return None if no arguments are provided
    
    min_number = args[0]  # Initialize max_number with the first argument
    for number in args:
        if number < min_number:
            min_number = number
    return min_number

# Input tuple of numbers from the user
user_input = input("Enter a tuple of numbers separated by commas: ")

# Split the input string at commas and convert each part into an integer
numbers_list = [int(num) for num in user_input.split(',') if num.strip().isdigit()]

# Convert the list of numbers into a tuple
numbers_tuple = tuple(numbers_list)

# Example usage:
minimum = find_min(*numbers_tuple)
if minimum is not None:
    print("The minimum number among the given tuple values is:", minimum)
else:
    print("No valid tuple values provided.")
user_input = input("Enter a tuple of numbers separated by commas: ")
numbers_list = [int(num) for num in user_input.split(',') if num.strip().isdigit()]
numbers_tuple = tuple(numbers_list)
total = sum(numbers_tuple)
average = total / len(numbers_tuple)
print("average is:")
print(average)
