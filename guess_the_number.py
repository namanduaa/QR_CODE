import random

target = random.randint(1, 100)

while True:
    try:
        guess = int(input("guess the number: "))
        if guess < target:
            print("low guess")
        elif guess > target:
            print("high guess")
        elif guess == target:
            print("congratulations")
            break
    except ValueError:
             print("invalid number")


