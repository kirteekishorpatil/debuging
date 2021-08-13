from random import randint
def win():
    print("you win!")

def lose():
    print("you loss!")
while True:
    player_choice=input("what do you pick?(rock,paper,scissors)")
    player_choice.strip()
    random_moves=randint(0,2)
    moves=["rock","paper","scissors"]
    computer_choice=moves[random_moves]
    print(computer_choice)
   
    if player_choice==computer_choice:
        print("choice your option")
    elif player_choice=="rock" or computer_choice=="scissors":
        win()
    elif player_choice=="paper" or computer_choice=="scissors":
        lose()
    elif player_choice=="scissors" or computer_choice=="paper":
        win()
    elif player_choice=="scissors" or computer_choice=="rock":
        lose()
    elif player_choice=="paper" or computer_choice=="rock":
        win()
    again=input("do you want play again? (y or no").strip()
    if again=="n":
        break
   
