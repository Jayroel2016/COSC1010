#
# Luke Jayroe
# Date
# Average of Numbers Programming Project
# COSC 1010
#
# define main function
def main():
    #open file
    myfile = open('numbers.txt', 'r')
   #variables 
    total = 0
    numberOfLines = 0
    line = myfile.readline()

    while line != "":
        numberOfLines += 1
        total += total + int(line)
        line = myfile.readline()
#instructions to find average
    average = total / numberOfLines

    print( "The average is", average )