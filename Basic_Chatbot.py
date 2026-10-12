
# CodeAlpha Internship - Task 4
# Basic Chatbot

def chatbot_response(message):
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi! Welcome to the chatbot."

    elif message == "how are you":
        return "I'm fine, thanks! How are you?"

    elif message == "what is your name":
        return "I am CodeBot, your Python chatbot."

    elif message == "what can you do":
        return "I can chat with you and answer simple messages."

    elif message == "thank you" or message == "thanks":
        return "You're welcome!"

    elif message == "bye" or message == "goodbye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that message."


def start_chatbot():
    print("=" * 40)
    print("       WELCOME TO CODEBOT")
    print("=" * 40)
    print("Type 'bye' to exit the chatbot.")
    print()

    while True:
        user_message = input("You: ")
        response = chatbot_response(user_message)

        print("CodeBot:", response)

        if user_message.lower().strip() in ["bye", "goodbye"]:
            break


# Start the chatbot
start_chatbot()
