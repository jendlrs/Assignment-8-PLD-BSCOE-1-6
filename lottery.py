#Assignment 8

#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

import random

def lottery():
    while True:
        luckynumbers = random.sample (range (0,9),3) #This will generate 3 winning numbers
        try:
            while True:
                first_ = int (input ("Enter your first number: "))
                if first_ >9 or first_ <=-1:
                    print ("Make sure that your number is ranging 0 to 9.") 
                    continue #if the user enters a number that is greater than 9 or a negative number, it will ask for 1st number again.
                while True:
                    second_ = int (input("Enter your second number: "))
                    if second_ >9 or second_ <=-1:
                        print ("Make sure that your number is ranging 0 to 9.")
                    while True:
                        third_ = int (input("Enter your third number: "))
                        if third_ >9 or third_ <=1:
                            print ("Make sure that your number is ranging 0 to 9.")
                        else:
                            return first_, second_, third_
        except ValueError:
            print ("Invalid Input! Make sure to enter numbers only.")
            ready = input ("Do you want to try again? y/n ")
            if ready == 'y':
                continue
            else:
                print ("Thank you for playing Jensen's lottery.")

first, second, third = lottery()
