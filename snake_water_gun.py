import random

dict = {
    1:"snake" ,
    -1: "water" , 
    0:"gun",
}
random_choice = random.choice([1,-1,0])  
print(" -- 1 for snake, -1 for water, 0 for gun -- ")
yourchoice = int(input("enter your choice  :"))

computer = dict[random_choice]  #computer stores snake,water,gun from dict 
print(f"computer random choice is : {random_choice}")
you = dict[yourchoice]       #you stores snake,water,gun from dict 

if computer == "snake" and you == "water":   # computer,you checks snake,wwater ,gun
    print("computer wins the game.")
elif computer == "snake" and you == "gun":
    print("you wins the game.")

elif computer == "water" and you == "gun":
    print("computer wins the game.")
elif computer == "water" and you == "snake":
    print("you wins the game.")

elif computer == "gun" and you == "water":
    print("you wins the game.")
elif computer == "gun" and you == "snake":
    print("computer wins the game.")

elif computer == you:
    print("it is a draw")
else:
    print("--------crash---------")