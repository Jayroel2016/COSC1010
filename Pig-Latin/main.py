#
# Luke Jayroe
# 4/18/25
# Pig Latin Programming Project
# COSC 1010
#
def main():
    # Ask the user for input
    sentence = input("Enter a sentence in English: ")

    # Split the sentence into words using string methods
    words = sentence.split()

    # Initialize an empty string to build the result
    pig_latin_sentence = ""

    # Loop through each word and convert to Pig Latin
    for word in words:
        if len(word) > 1:
            pig_word = word[1:] + word[0] + "ay"
        else:
            pig_word = word + "ay"
        
        # Add the Pig Latin word to the sentence
        pig_latin_sentence += pig_word + " "

    # Remove trailing space and print the result
    print("Pig Latin:", pig_latin_sentence.strip())

# Run the program
main()