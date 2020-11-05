import random

number = random.randint(1,100)
attempts = 0
count = 100
while attempts<10:
    attempts +=1
    guess = int(input("Guess a number between 1 to 100:"))
    if (guess < number):
        count -=10
        print("Guess higher")   
    elif (guess > number):
        count -=10
        print("Guess lower")
    else:
        print("Guessed !")
        break
print("Game Over , you took ",attempts,"the number was ",number,"and scored",count)
