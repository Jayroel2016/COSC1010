#
# Luke Jayroe
# 4/9/25
# Lottery Number Generator Programming Project
# COSC 1010
#
import random

MAX_DIGITS = 7
START = 0
END = 9

# Main function
def main ():
    # Making list
    numbers = [0] * 7

    # Populating list with random numbers
    for index in range (MAX_DIGITS) :
        numbers[index] = random.randint (START, END)

    # Display random list
    print ('Here are your lottery numbers:')
    for index in range (MAX_DIGITS) :
        print(numbers[index], end='')
        print()

# Call main function
main ()
