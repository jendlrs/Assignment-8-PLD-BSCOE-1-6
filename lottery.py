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
        print (luckynumbers)
        break

lottery()