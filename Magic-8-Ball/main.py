#
# Luke Jayroe
# 4/9/25
# Magic 8 Ball Programming Project
# COSC 1010
#
import random

def magic_8_ball():
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later.",
        "I'm not sure.",
        "I can't tell you right now.",
        "I will tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO."
    ]

    print("Welcome to the Magic 8 Ball!")
    print("Ask a yes/no question, or type 'quit' to exit.")

    while True:
        question = input("\nAsk your questions mortal! ")
        if question.lower() in ['quit', 'exit']:
            print("Farewell mortal, come back if you have more unanswered questions.")
            break
        elif question.strip() == "":
            print("Please ask a yes or no question.")
        else:
            answer = random.choice(responses)
            print(f" {answer}")

# Run the program
if __name__ == "__main__":
    magic_8_ball()