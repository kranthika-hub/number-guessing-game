import random

print("Welcome to the Number Guessing Game!")

print("Choose difficulty:")
print("1. Easy (1–50)")
print("2. Medium (1–100)")
print("3. Hard (1–200)")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    number = random.randint(1, 50)
elif choice == 2:
    number = random.randint(1, 100)
else:
    number = random.randint(1, 200)

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
        print("Total attempts:", attempts)
        break
