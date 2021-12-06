#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.
import random

print ("\nWelcome to Number Guessing Game")
name = input ("\nWhat is your name? ")
print (f"Hi {name}! This game will generate one mystery number that you will have to guess.")

def guess_number ():
    number_ = random.randrange(0,100)
    while True:
        user_guess = int(input("\nWhat is your guess? "))
        if user_guess == number_:
            print (f"\nCongratulations! You got it right. The correct number is {number_}.")
            break
        elif user_guess > number_:
            print ("\nWRONG")
            print ("Hint: Your input is GREATER THAN the random number to be guess.")
        else:
            print ("\nWRONG")
            print ("Hint: Your input is LESS THAN the number to be guess.")

guess_number()
