#
# Luke Jayroe
# 4/18/25
# Vowels and Consonants Programming Project
# COSC 1010
#
# Main function
def main():
    # Get string from user
    user_str = input('Enter a string of characters: ')  # Fixed 'inpuut' to 'input' and added colon

    # Report the vowels and consonants
    print('That string has', num_vowels(user_str), 'vowels and', num_consonants(user_str), 'consonants.')  # Fixed backslash and formatting

# The num_vowels function returns the number of
# vowels in the string passed as an argument.
def num_vowels(s):  # Parameter name should be consistent (s, not S)
    # Make a list containing the vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize the accumulator
    v_count = 0

    # Count the vowels in s
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1

    # Return the vowel count
    return v_count

# The num_consonants function returns the number of
# consonants in the string passed as an argument.
def num_consonants(s):
    # Make a vowel list
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Fixed bracket type (was a mix of set and list)

    # Initialize the accumulator
    c_count = 0

    # Count the consonants in s
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1
            
    # Return the consonant count
    return c_count

# Call the main function
main()