#
# Luke Jayroe
# 3/2/25
# Budget Analysis Programming Project
# COSC 1010
#
# Establishing the budget

userbudget = float( input ("Please enter how much you have budgeted for the month:" ))

#variables

total = 0

another = 'y'

#establishing the expenses taken from budget

while another == 'y' or another == 'Y':
    expense = float(input('Please enter the amount of your expense:'))
    total += float(expense)
    another = input('Do you want to enter another amount? enter y or Y for yes:')

#finishing formula 

print(userbudget - total)