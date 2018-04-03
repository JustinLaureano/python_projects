from random import randint

num = randint(1, 11)
num_of_guesses = 1
guess = int(input("Guess a number between 1 and 10\n"))

if guess == num:
    print("First try")

while guess != num:

    if guess < num:
        num_of_guesses += 1
        print("guess higher")
        guess = int(input("Guess a number between 1 and 10\n"))

    elif guess > num:
        num_of_guesses += 1
        print("guess lower")
        guess = int(input("Guess a number between 1 and 10\n"))


print("You guessed it in {} tries".format(num_of_guesses))

