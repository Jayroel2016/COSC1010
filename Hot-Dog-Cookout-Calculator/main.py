#
# Luke Jayroe
# 2/19/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Constants
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Local variables
numAttending = 0    # The number of people attending
numPerPerson = 0    # The number of hotdogs and buns per person
total = 0   # The total number of hotdogs and buns needed.
minDogs = 0     # The minimum number of packages of hotdogs.
minBuns = 0     # The minimum number of packages of buns.
dogsLeft = 0    # The amount of hotdogs leftover from a package.
bunsLeft = 0    # The amount of buns leftover from a package.

# Get the number of people attending the cookout from the user.
numAttending = int(input('Enter the number of people attending: '))

# Get the number of hotdogs per person from the user.
numPerPerson = int(input('Enter the number of hotdogs per person: '))

# Calculate the total number of hotdogs and buns needed.
total = numAttending * numPerPerson

# Calculate the minimum number of packages of hotdogs needed.
minDogs = total // HOT_DOGS_PER_PACKAGE

# Determine if the total number of people attending is large enough to require more than one package of hotdogs.
if minDogs > 0:
    #Calculate the amount of hotdogs leftover from a package, if any.
    dogsLeft = total % HOT_DOGS_PER_PACKAGE

     # If there will be leftovers, add an additional package of hotdogs.
    if dogsLeft != 0:
        minDogs += 1
     
# Set the minumum number of packages of hotdogs to one.
else:
    minDogs = 1 
# Determine the amount of leftover hot dogs, if any.
dogsLeft = HOT_DOGS_PER_PACKAGE * minDogs - total

# Calculate the minimum number of packages of buns needed.
minBuns = total // BUNS_PER_PACKAGE

# Determine if the total number of people attending is large enough to require more than one package of buns.
if minBuns > 0:
    #Calculate the amount of buns leftover from a package, if any.
    bunsLeft = total % BUNS_PER_PACKAGE

     # If there will be leftovers, add an additional package of buns.
    if bunsLeft != 0:
        minBuns += 1
else:
    minBuns = 1 

# Determine the amount of leftover buns, if any.
bunsLeft = BUNS_PER_PACKAGE * minBuns - total

# Display the minimimum packages of hotdogs needed.
print('Minimum packages of hotdogs needed: ', minDogs)

# Display the minimum packages of buns needed.
print('Minumum packages of buns needed: ', minBuns)

# Display the amount of hotdogs leftover.
print('Hotdogs left over: ', dogsLeft)

# Display the amount of buns leftover.
print('Buns leftover: ', bunsLeft)