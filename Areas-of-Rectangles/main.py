#
# Luke Jayroe
# 2/19/2025
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
lenght1 = 0
width1 = 0
length2 = 0
width2 = 0
area1 = lenght1 * width1
area2 = length2 * width2
# Get length A
length1 = int (input ('Enter the lenght of rectangle 1: '))
# Get width A
width1 = int (input ('Enter the width of rectangle 1: '))
# Get length B
length2 = int (input ('Enter the length of rectangle 2: '))
# Get width B
width2 = int (input ('Enter the width of rectangle 2: '))
# Calculate area A
area1 = length1 * width1
# Calculate area B
area2 = length2 * width2
# Print area comparison using if-elif-else statements
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print ('Rectangle 2 has the greater area.')
else:
    print ('Both have the same area.')