
import random
import math


print("="*50)

num = round(random.random () * 100)


print(f"You have 10 guesses")
attempts = 0
max_attempts = 10
 
while attempts < max_attempts:
    guessnum = int(input("Number from 0-100: "))
    attempts += 1

    if guessnum > 100:
        print("Error number higher then 100")
    elif guessnum > num:
        print("Too high guess again")
    elif guessnum < num:
        print("Too low guess again")
    else:
        print("You Win!🏆")

if guessnum != num:
    print(f"Out of attempts :( , the correct number is {num} ")

print("Game over")

print("="*50)