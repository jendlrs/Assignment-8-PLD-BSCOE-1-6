#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.
import random
import time

print ("\nWelcome to Number Guessing Game")
name = input ("\nWhat is your name? ")
print (f"\nHi {name}! This game will generate one mystery number that you will have to guess.")
time.sleep (0.5)
print ("\nGenerating mystery number....")
time.sleep (1.5)
print ("\nThe mystery number is ready.")
time.sleep (1)

def guess_number ():
    number_ = random.randrange(0,100)
    while True:
        try:
            user_guess = int(input("\nWhat is your guess? "))
            if user_guess == number_:
                print (f"\nCongratulations! You got it right. The mystery number is {number_}.\n")
                break
            else:
                if user_guess >100 or user_guess <=-1:
                    print ("\nMake sure that you have entered a number ranging 0 to 99.")
                    continue
                elif user_guess > number_:
                    print ("\nWRONG")
                    print ("Hint: Your input is GREATER THAN the mystery number. Try reducing it.")
                    continue
                else:
                    print ("\nWRONG")
                    print ("Hint: Your input is LESS THAN the mystery number. Try increasing it.")
                    continue
                
        except ValueError:
            print ("This program only accepts number. Try again.")
            continue

guess_number()
