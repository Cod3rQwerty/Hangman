import random
import os

curdir = os.path.dirname(os.path.abspath(__file__))

#function to get words
def readFile(path):
    try:
        with open(path, "r") as file:
            ReadWords = file.read().splitlines()
        return ReadWords
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        exit(1)

while True:
    #define list of words, number of attempts till fail and reset Correctletters
    #and GuessedLetters.Also, you can change attempts and add words to words list
    words = readFile(curdir + "\\Words.txt")
    CorrectLetters = []
    attempts = 11

    #choose answer randomly from the list of words
    answer = random.choice(words)
    anslen = len(answer)
    
    #reset CorrectLetters to _____ to indicate that the player hasnt
    #gotten any letters right so far.
    for i in range(anslen):
        CorrectLetters.append("_")
    
    while True:
        #print out CorrectLetters on one line
        for char in CorrectLetters:
            print(char, end="")
        
        print() # creates a newline

        #output number of attempts left and takes input from user 
        print(f"You have {attempts} attempts left.")
        guess = input("What letter or word would you like to guess? Guess: ").lower()

        attempts -= 1 #decreases attempts by 1

        if len(guess) == 1: #logic for single letter guess
            if guess in answer:
                #if guess is correct...
                print(f"Guess Correct! {guess} is in the word.", end="\n\n")

                #what this does is go through each item in
                #CorrectLetters and replace it with the guess if
                #it is in that position in the answer
                for idx, char in enumerate(CorrectLetters):
                    if answer[idx] == guess:
                        CorrectLetters[idx] = guess
            else:
                #if guess is wrong:
                print(f"Guess wrong! {guess} is not in the word.", end="\n\n")
        else:
            #this is if the user input a word.
            if guess == answer:
                #if user inputs the answer, they win instantly
                print("You win!")
                print("Starting new game...")
                print()
                break
            else:
                #if user's guess is wrong:
                print(f"Guess wrong! {guess} is not the word.", end="\n\n")

        #checks to see if the user has won by guessing all letters.
        if not "_" in CorrectLetters:
            print("You win!")
            print("Starting new game...")
            print()
            break
        
        #checks to see if the user has lost by losing all attempts
        if attempts == 0:
            print(f"You lose! The word was {answer}")
            break
