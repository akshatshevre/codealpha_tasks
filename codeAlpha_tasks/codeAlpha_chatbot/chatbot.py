def get_bot_response(user_input):

    # Convert input to lowercase so the bot isn't confused by capital letters

    user_input = user_input.lower().strip()


    # Rule-based logic using if-elif-else

    if user_input == "hello" or user_input == "hi":

        return "Hi there! How can I help you today?"

    elif user_input == "how are you":

        return "I'm doing great, thanks for asking! How are you?"

    elif user_input == "bye" or user_input == "goodbye":

        return "Goodbye! Have a great day!"

    else:

        return "I'm sorry, I don't understand that. I'm a simple bot!"



def start_chatbot():

    print(" Chatbot: Hello! I am a simple rule-based bot.")

    print("(Type 'bye' to exit the conversation)\n")


    # Infinite loop to keep the conversation going until the user says bye

    while True:

        # Get input from the user

        user_message = input("You: ")


        # Get the bot's response based on the input

        bot_reply = get_bot_response(user_message)


        # Print the bot's response

        print(f" Chatbot: {bot_reply}\n")


        # Break the loop and end the program if the user says goodbye

        if user_message.lower().strip() in ["bye", "goodbye"]:

            break



# This triggers the chatbot to run when you execute the script

if __name__ == "__main__":

    start_chatbot()

