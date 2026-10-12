# PYTHON PROGRAMMING PROJECTS

# 1. HANGMAN GAME

## Introduction
Hangman is a text-based word-guessing game developed using Python. The computer randomly selects a word from a predefined list, and the player tries to guess the word by entering one letter at a time.

## Objective
To develop an interactive word-guessing game using Python programming concepts.

## Features
- Selects a random word from a list of five words.
- Allows the player to guess one letter at a time.
- Displays correctly guessed letters.
- Allows a maximum of six incorrect guesses.
- Displays a winning or losing message.

## Working
The program selects a random word and displays its letters as blanks. The player enters a letter, and the program checks whether it exists in the word. Correct guesses reveal the letters, while incorrect guesses reduce the remaining attempts. The game ends when the word is guessed or the attempts are exhausted.

## Technologies Used
Python, random module, lists, strings, loops, conditional statements, and user input.

## Conclusion
The Hangman Game demonstrates the use of basic Python concepts to create an interactive game. It improves logical thinking and understanding of loops, strings, and conditional statements.

---

# 2. STOCK PORTFOLIO TRACKER

## Introduction
The Stock Portfolio Tracker is a Python application that calculates the total investment value of selected stocks. It uses predefined stock prices and allows users to enter stock symbols and quantities.

## Objective
To develop a program that calculates the value of stock holdings using dictionaries and basic arithmetic operations.

## Features
- Displays available stocks and their prices.
- Accepts stock symbols and quantities.
- Checks whether the entered stock symbol is valid.
- Calculates the investment value of each stock.
- Calculates the total investment value.
- Saves the portfolio report in a text file.

## Working
The program stores stock symbols and their prices in a dictionary. The user enters a stock symbol and the number of shares. The program multiplies the price by the quantity to calculate the investment value. After the user finishes entering stocks, the program displays the portfolio report and total investment and saves the result in a text file.

## Formula
Investment Value = Stock Price × Quantity

Total Investment = Sum of all individual stock investment values.

## Technologies Used
Python, dictionaries, loops, conditional statements, arithmetic operations, exception handling, and file handling.

## Conclusion
The Stock Portfolio Tracker demonstrates how Python can be used to automate financial calculations and organize investment information. It provides practical experience with dictionaries, input validation, and file handling.

Note: This project uses predefined sample stock prices and does not retrieve live market prices or calculate actual profit and loss.

---

# 3. BASIC CHATBOT

## Introduction
The Basic Chatbot is a simple conversational program developed using Python. It accepts messages from the user and responds with predefined replies based on the entered text.

## Objective
To develop a basic rule-based chatbot using Python functions, loops, and conditional statements.

## Features
- Responds to greetings such as "hello" and "hi".
- Answers predefined questions such as "how are you".
- Introduces itself as CodeBot.
- Responds to messages such as "thank you".
- Displays a default response for unknown messages.
- Ends the conversation when the user enters "bye" or "goodbye".

## Working
The chatbot accepts a message from the user and converts it to lowercase while removing extra spaces at the beginning and end. It checks the message against predefined conditions and displays the appropriate response. The conversation continues until the user enters an exit message.

## Technologies Used
Python, functions, loops, conditional statements, string methods, and input/output operations.

## Conclusion
The Basic Chatbot demonstrates how a computer program can simulate simple conversations using predefined rules. It provides a foundation for understanding interactive applications and chatbot development.

---

# OVERALL CONCLUSION

These three Python projects demonstrate practical applications of programming fundamentals. The Hangman Game focuses on interactive gameplay, the Stock Portfolio Tracker performs investment calculations, and the Basic Chatbot simulates simple conversations. Together, they demonstrate the use of data structures, functions, loops, conditional statements, user input, and file handling in Python.

# FUTURE SCOPE

- **Hangman Game:** Add difficulty levels, a scoring system, and more words.
- **Stock Portfolio Tracker:** Add live stock prices, database storage, and profit/loss calculations.
- **Basic Chatbot:** Add more responses, a graphical interface, and natural language processing.

