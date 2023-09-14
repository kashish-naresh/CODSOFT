from random import *

def game():
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\tRock-Paper-Scissors!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\tEnter your choice: \n")
    print("\tChoice 1: Rock")
    print("\tChoice 2: Paper")
    print("\tChoice 3: Scissors\n")

    while True:
        user_choice = eval(input("\tSelect option from 1-3 : "))

        if user_choice > 3:
            print("\n\tPlease enter One Number from 1, 2, 3 ")
        else:
            break
        
    machine_choice = randint(1, 3)  

    print("\n\tComputer's Choice is :\n")
    if machine_choice == 1:
        print("\tRock")
    elif machine_choice == 2:
        print("\tPaper")
    else:
        print("\tScissors")

    print("\n")
    
    #making logic
    if user_choice == machine_choice:
        print("\tIt's a tie")
        
    elif user_choice == 1 and machine_choice == 3:
        print("\tYou Won!")
        
    elif user_choice == 2 and machine_choice == 1:
        print("\tYou Wom!")
        
    elif user_choice == 3 and machine_choice == 2:
        print("\tYou Won!")
        
    else:
        print("\tOopS Computer Won!")
        
    replay = input("\n\tWanna Play Again? (y/n) : ").lower()

    if replay =='y':
        game()
    else:
        print("\n\tThanks for playing!")
        
game()