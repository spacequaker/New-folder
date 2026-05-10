guess = int(input("guess a number between 1 and 10:" ))
if guess == 5:
    print("You guessed it!")
elif guess < 5:
    print("Too low!")
else:    print("Too high!")