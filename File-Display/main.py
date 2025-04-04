#
# Luke Jayroe
# 4/4/25
# File Display Programming Project
# COSC 1010
#
# Opening the file
myfile = open('numbers.txt', 'r') 

# Read and display file's contents
for line in myfile:
    number = int(line)
    print(number)

# Close File
myfile.close()


# Error message saying i do not have the numbers.txt file.