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
print ("Generating mystery number....")
def guess_number ():
    number_ = random.randrange(0,100)
    while True:
        try:
            while True:
                user_guess = int(input("\nWhat is your guess? "))
                if user_guess >100 or user_guess <=-1:
                    print ("Make sure that you have entered a number ranging 0 to 99.")
                    continue
                while True:
                    if user_guess == number_:
                        print (f"\nCongratulations! You got it right. The correct number is {number_}.\n")
                        break
                    elif user_guess > number_:
                        print ("\nWRONG")
                        print ("Hint: Your input is GREATER THAN the random number to be guess.")
                        break
                    else:
                        print ("\nWRONG")
                        print ("Hint: Your input is LESS THAN the number to be guess.")
                        break
                
        except ValueError:
            print ("This program only accepts number. Try again.")
            continue

guess_number()
