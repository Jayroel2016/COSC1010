#
# Luke Jayroe
# 3/7/25
# Feet to Inches Programming Project
# COSC 1010
#
# Constant
INCHES_PER_FOOT = 12

#Define main function
def main():
    #Get input from user
    feet = int(input('Enter a number of feet: '))
    
    #Convert input to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

#The feet_to_inches function converts the feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

#Call the main function
main()
