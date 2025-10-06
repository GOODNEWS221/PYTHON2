import random

print("                              ")
print("          WELCOME             ")

print("in this game the user is to pick a choice vs computer choice")


Trial = 0


while True:
    try: 
        computer_choice = random.randint(1, 9)
        player_choice = int(input("pick your choice between 1-9: "))
        print(f"your choice is: {player_choice}")
        print(f"Computer choice is: {computer_choice}")
        Trial += 1
        

        if player_choice == computer_choice:
            print("You won")
            print(f"you attempted this: {Trial} times")
            break
            

        elif player_choice != computer_choice: 
            print("you lost")

        else:
            print("Invalid, please try again")

        

    except ValueError:
        print("invalid choice, choose between 1 -9")







