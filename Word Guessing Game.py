import random
name = input("What is your name:")

companies = ['Facebook','Apple','Netflix','Google','Amazon','Microsoft','Adobe']
company = random.choice(companies)

print("Hey",name,"guess a tech company!")
guesses = ''
attempts = 10

while attempts > 0:
    fail = 0
    for char in company:
        if char in guesses:
            print(char)
        else:
            print("_")
            fail += 1
    if fail == 0:
        print("You won.The word is:",company)
        break
    guess = input("Guess a tech company:")
    guesses += guess
    if guess not in company:
        attempts -= 1
        print("Wrong")
        print("You have",attempts,"more guesses")
    if attempts == 0:
        print("You lost")
