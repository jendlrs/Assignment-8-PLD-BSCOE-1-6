#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.
import random

def guess_number ():
    number_ = random.randrange(0,100)
    while True:
        user_guess = int(input("What is your guess? "))
        if user_guess == number_:
            print (f"Congratulations! You got it right. The number is {number_}.")
            break

guess_number()
