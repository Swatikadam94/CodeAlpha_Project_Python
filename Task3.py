import random

# Predefined responses
responses = {
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a bunch of code, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that. Can you rephrase?"
}

def chatbot():
    print("Welcome to Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye! Take care.")
            break
        response = responses.get(user_input, responses["default"])
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()