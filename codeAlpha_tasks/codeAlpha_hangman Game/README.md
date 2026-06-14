hangman game - Breakdown of Key Concepts Used:

1. random.choice() (Picking a Random Word)

Instead of writing a massive block of logic just to pick a word, we imported the random library and handed it our list of 5 words. The random.choice(words) function simply picks one random word from that list every time the script runs. Think of it like blindly drawing a single card from a shuffled deck.

2. while Loop (The Game Engine)

This is the heart of the game. Without this loop, the script would ask for a letter exactly once and immediately shut down. We set a simple rule: "Keep asking the player for inputs as long as they haven't messed up 10 times." The moment they win, or hit 10 wrong attempts, a break statement triggers, and the loop stops.

3. Lists (Data Storage)

We used two lists to keep track of things:

• words: This is our permanent word bank where the game selects the hidden word.

•guessed: This starts completely empty. Every time the player types a valid letter, we use .append() to shove it into this list. This acts as the game's memory, so if the player types the same letter again, the code can instantly say, "Hey, you already tried that one!"

4. Word Rebuilding (The _ Logic)

This is the coolest part of the logic. Every single time the player hits Enter, the code clears the display and checks the secret word character-by-character from scratch. It loops through the word and checks the guessed list:

• If the letter is in the list, it reveals the actual letter.

• If not, it just prints a _.
This entire string is rebuilt fresh on every single turn.

5. if-else (The Game Rules)

This handles the decision-making and enforces the rules. As soon as the player inputs a letter, it goes through a quick chain of checkposts:

• Typed more than one letter? \rightarrow Reject it.

• Typed a duplicate letter? \rightarrow Warn them.

•Is the letter in the word? \rightarrow Say "Correct!".

•Not in the word? \rightarrow Deduct a life.

6. Input Sanitizing (Handling Messy Inputs)

Players can be messy—they might type a capital 'A' instead of 'a', or accidentally hit a number like '5'. To stop the game from crashing:

• .lower() forces every input into lowercase so the code doesn't get confused between 'P' and 'p'.

• .isalpha() acts like a bouncer at the door; if a user types a number or a symbol, it kicks it out immediately and asks for a proper letter.

