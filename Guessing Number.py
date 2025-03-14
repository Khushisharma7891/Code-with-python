import random

lower_bound = 1
upper_bound = 100

random_number = random.randint(lower_bound, upper_bound)

max_attempts = 10
attempts_left = max_attempts

print("Welcome to 'Guess the Number'!")
print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
print(f"You have {max_attempts} attempts to guess it.")

while attempts_left > 0:
    print(f"\nYou have {attempts_left} attempts left.")
    
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {random_number} correctly!")
        break

    attempts_left -= 1

if attempts_left == 0:
    print(f"\nSorry, you ran out of attempts. The correct number was {random_number}.")
