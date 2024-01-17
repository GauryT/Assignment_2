# Define a function named 'separate_and_convert' that takes a string 's' as input
def separate_and_convert(s):
    # Initialize two empty lists to store the number and letter substrings
    num_list = []
    letter_list = []

    # Loop through the string 's'
    for char in s:
        # If the character is a digit, append it to the number list
        if char.isdigit():
            num_list.append(char)
        # If the character is a letter, append its lowercase equivalent to the letter list
        elif char.isalpha():
            letter_list.append(char.lower())

    # Convert the number list to a list of integers
    num_list = [int(num) for num in num_list]

    # Convert the letter list to a list of ASCII codes for even-indexed letters
    letter_list = [ord(char) for idx, char in enumerate(letter_list) if idx % 2 == 0]

    # Initialize two empty lists to store the ASCII codes for even numbers and even-indexed letters
    num_ascii_list = []
    letter_ascii_list = []

    # Append the ASCII codes for even numbers to 'num_ascii_list'
    num_ascii_list = [ord(str(num)) for num in num_list if num % 2 == 0]

    # Append the ASCII codes for even-indexed letters to 'letter_ascii_list'
    letter_ascii_list = [ascii_code for ascii_code in letter_list]

    # Return the two lists, 'num_ascii_list' and 'letter_ascii_list'
    return num_ascii_list, letter_ascii_list

# Get input string from user
s = input("Enter a string with numbers and letters (at least 16 characters long): ")

# Check if the length of the input string is at least 16
if len(s) >= 16:
    # Call the 'separate_and_convert' function and store the result in 'num_ascii_list' and 'letter_ascii_list'
    num_ascii_list, letter_ascii_list = separate_and_convert(s)

    # Print the ASCII codes for numbers
    print("ASCII Codes for Numbers:", num_ascii_list)

    # Print the ASCII codes for letters
    print("ASCII Codes for Letters:", letter_ascii_list)

# If the length of the input string is less than 16, print an error message
else:
    print("Input string must be at least length of 16.")