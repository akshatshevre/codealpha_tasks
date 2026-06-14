BASIC CHATBOT -Breakdown of Key Concepts Used:

• Functions (def): get_bot_response handles the logic of matching words, while start_chatbot manages the actual running game loop.

• Loops (while True): Keeps the chatbot running continuously so you can have a back-and-forth conversation instead of the program closing after just one question.

• Input/Output (input() / print()): Captures what you type in the terminal and displays the bot's replies.

• Conditional Logic (if-elif-else): Checks your exact words and pairs them with the predefined replies. .lower().strip() is added to make sure it still works if you accidentally type "HELLO " or "Bye".

