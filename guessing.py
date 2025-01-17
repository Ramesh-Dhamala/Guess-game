import random
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break