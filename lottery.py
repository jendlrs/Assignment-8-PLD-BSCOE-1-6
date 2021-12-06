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
print ("\nWelcome to Jensen's Lottery!")
name= input ("\nWhat is your name? ")
print (f"\nHi {name}! Are you feeling lucky today? This lottery system will ask you to enter three (3) numbers ranging from zero (0) to nine (9).")
print ("\nThen the system will automatically generate three (3) lucky numbers.")
print ("\nIf the three (3) lucky numbers match all of your numbers, you are a winner.")

def lottery():
    while True:
        luckynumbers = random.sample (range (0,9),3) #This will generate 3 winning numbers
        try:
            while True:
                first_ = int (input ("\nEnter your first number: "))
                if first_ >9 or first_ <=-1:
                    print ("\nMake sure that your number is ranging 0 to 9.") 
                    continue #if the user enters a number that is greater than 9 or a negative number, it will ask for 1st number again.
                while True:
                    second_ = int (input("Enter your second number: "))
                    if second_ >9 or second_ <=-1:
                        print ("\nMake sure that your number is ranging 0 to 9.")
                        continue
                    elif first_ == second_ :
                        print ("\nYou already picked that number")
                        continue
                    else:
                        break
                while True:
                    third_ = int (input("Enter your third number: "))
                    if third_ >9 or third_ <=1:
                        print ("\nMake sure that your number is ranging 0 to 9.")
                        continue
                    elif third_ == second_ or third_ == first_:
                        print ("\nYou already picked that number")
                        continue
                    else:
                        break
                break
            
            user_input = first_, second_, third_
            print (f"\nThe numbers you entered are {user_input}")
            
            match = 0 

            for i in luckynumbers:
                if (i== first_ or i == second_) or i== third_:
                    match= match +1 #match is incremented by 1
            if match == 3:
                print (f"\nThe winning numbers are {luckynumbers}. \nCongratulations! You won!")
            else:
                print (f"\nYou Loss. The winning numbers are {luckynumbers}")
                ready =input ("\nDo you want to try again? y/n ")
                if ready == "y":
                    continue
                else:
                    print ("\nThank you for using Jensen's Lottery!\n") #Exit
                    break
            
        except ValueError:
            print ("\nInvalid Input! Make sure to enter numbers only.")
            ready = input ("\nDo you want to try again? y/n ")
            if ready == 'y':
                continue
            else:
                print ("\nThank you for using Jensen's lottery.\n") #Exit

lottery()
