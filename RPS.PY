import random

# dict = {"r": "🪨", "p": "📋", "s": "✂️"}
while True:
    computer_choice = random.choice(["r", "p", "s"])
    user_choice = input("Rock, paper, scissor ?(r/p/s): ")
    dict = {"r": "🪨", "p": "📋", "s": "✂️"}
    if user_choice not in dict:
        print("invalid choice")
        continue

    if user_choice == computer_choice:
        print(f"computer choose {dict[computer_choice]}\nyou choose {dict[user_choice]}")
        print("it's a tie!")
    elif computer_choice == "r" and user_choice == "p":
        print(f"computer choose {dict[computer_choice]}\nyou choose {dict[user_choice]} ")
        print("you win")
    elif computer_choice == "r" and user_choice == "s":
        print(f"computer choose {dict[computer_choice]}\n" "you choose  {dict[user_choice]}")
        print("you lose")
    elif computer_choice == "p" and user_choice == "r":
        print(f"computer choose  {dict[computer_choice]}\nyou choose {dict[user_choice]}")
        print("you lose")
    elif computer_choice == "p" and user_choice == "s":
        print(f"computer choose {dict[computer_choice]} \nyou choose {dict[user_choice]}")
        print("you win")
    elif computer_choice == "s" and user_choice == "r":
        print(f"computer choose  {dict[computer_choice]}\nyou choose {dict[user_choice]}")
        print("you win")
    elif computer_choice == "s" and user_choice == "p":
        print(f"computer choose  {dict[computer_choice]}\nyou choose {dict[user_choice]}")
        print("you lose")
    elif user_choice == computer_choice:
        print("it is a tie")

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
        break
