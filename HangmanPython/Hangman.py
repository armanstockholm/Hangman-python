import functools
from mmap import PROT_READ
from operator import index, indexOf
import os
from random import randint
from xmlrpc.client import Boolean

while True:
    print("-------------------------------")
    print("--------------HANGMAN----------")
    print("-------------------------------")
    print("Hello, welcome to Hangman! ")

    gameWord = input("Enter a word to start the game \n")

    i_list = []
    for a in gameWord:
        i_list.append(a)

    wordlength = len(gameWord)
    secretWord = []
    underline = "_"
    guessedLetters = []
    for a in gameWord:
        secretWord.append(underline)    

    try:
        numberOfGuesses = int(input("Enter number of guesses \n"))
    except ValueError:
        print("Upps, you did not enter a correct value. You will get a random number between 5 and 15")
        numberOfGuesses = randint(5, 15)
    print("Lets start the game. You have ", numberOfGuesses, " guesses!")

    attempts = 0
    right = True
    guess = ""
    alreadyGuessed = False
    firstTime = True
    while True:
        

        print("-------------------------------")
        print("--------------HANGMAN----------")
        print("-------------------------------")
        if not firstTime:
            if right == False and alreadyGuessed == False:
                print(guess, " was wrong")
            if right == True and alreadyGuessed == False:
                print(guess, " was the right guess!")
        if alreadyGuessed == True:
            print("You have already guessed ", guess )
        if not firstTime:    
            print(" You have ", numberOfGuesses - attempts, " guesses left")
        print("Your guesses:")
        print(guessedLetters)
        for a in secretWord:
            print(a, end =" ")
        guess = input("\n enter guess: \n")
        
        alreadyGuessed = False
        
        for a in guessedLetters:
            if a == guess:
                alreadyGuessed = True
                
                
        if not alreadyGuessed: 
            attempts += 1       
            count = 0
            right = False
            for a in i_list:
                if a.lower() == guess.lower():
                    right = True
                    secretWord[count] = guess.lower()
                count += 1

            if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, secretWord, i_list)
            , True) or gameWord.lower() == guess.lower():
                print("You got the word!")
                print("it was", gameWord, "and it took you", attempts, "guesses")
                break  

            if attempts == numberOfGuesses:
                print("You exceeded the maximum number of guesses")
                print("correct answer is", gameWord)
                break 
            guessedLetters.append(guess)
        if attempts == numberOfGuesses:
            print("You exceeded the maximum number of guesses")
            print("correct answer is", gameWord)
            break 
        firstTime = False
        os.system('cls' if os.name == 'nt' else 'clear')

    playAgain = input("Would you like to play again? \n")
    if playAgain.lower() == "y" or playAgain.lower() == "yes":
        print("Lets start over!")
    else:
        break   



print("Thank you for playing!")

