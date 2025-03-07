#
# Luke Jayroe
# 3/7/25
# Kilometer Converter Programming Project
# COSC 1010
#
# Converting kilometers to miles
CONVERSION_FACTOR = 0.6214

#define the main funtion which is to convert kilometers to miles
def main():
    
    #Get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: ')) 

    #Show the distance converted to miles
    show_miles(kilometers)

#Define show_miles function
def show_miles(km):
    
    #Calculate miles
    miles = km * CONVERSION_FACTOR

    #Display the miles
    print(km, 'kilometers equal', miles, 'miles.')

#Call the main function
main()
