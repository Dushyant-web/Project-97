print("                                                        A Guessing Game")
import random

rand = random.randint(1,9)

chances = 0

print("Guess Any Number Between(1 to 9)")
print("But You Can Guess Just 5 Time")


while chances<5:
    guess = int(input("Enter your guess - "))

    if guess == rand:
        print("You Won!")
        print("                                               This Game Is Made By Dushyant")

        break
    
    elif guess < rand:
        print("Your Guess Is To Low ,hint - Guess a Higher Number")

    else:
        print("Your Guess Is To High ,hint - Guess a smaller Number")
    
    chances+=1

if chances==5 and guess!= rand:
    print("  Sorry Chances Over ")
    print("                                                   This Game Is Made By Dushyant")
