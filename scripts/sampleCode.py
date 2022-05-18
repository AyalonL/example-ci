import random

print("Guess the dice roll")
guess = input("What will the dice roll? ")

dice = random.randint(1, 6)

if int(guess) == dice:
	print(dice)
	print("You guessed correct")
else:
	print("The dice roll gave " + str(dice) + "! You Lost")

