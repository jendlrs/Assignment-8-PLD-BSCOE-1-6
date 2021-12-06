#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.
import random
import time

print ("\nWelcome to \033[33mNumber Guessing Game!\033[0m")
name = input ("\nWhat is your name? ")
print (f"\nHi \033[36m{name}!\033[0m This game will generate one mystery number that you will have to guess.")
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
                print (f"\n\033[1;32;40mCongratulations!\033[0;37;40m You got it right. The mystery number is \033[32m{number_}.\033[0m\n")
                break
            else:
                if user_guess >100 or user_guess <=-1:
                    print ("\n\033[1mMake sure that you have entered a number ranging 0 to 99.\033[0m")
                    continue
                elif user_guess > number_:
                    print ("\n\033[91mWRONG\033[0m")
                    print ("Hint: Your input is GREATER THAN the mystery number. Try reducing it.")
                    continue
                else:
                    print ("\n\033[91mWRONG\033[0m")
                    print ("Hint: Your input is LESS THAN the mystery number. Try increasing it.")
                    continue
                
        except ValueError:
            print ("This program only accepts number. Try again.")
            continue

guess_number()
