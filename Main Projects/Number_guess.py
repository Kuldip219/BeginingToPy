import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your number: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")