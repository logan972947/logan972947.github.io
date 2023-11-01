    # user chooses rock then program randomly chooses paper or scissors
    # user chooses paper then program randomly chooses rock or scissors
    # user chooses scissors then program randomly rock or paper

    # rock beats scissors
    # scissors beats paper
    # paper beats rock

    # rock is draw against rock
    # paper is draw against paper
    # scissors is draw against scissors

    #rock beats scissors

      
    #scissors beats paper
      
    # paper beats rock

    #paper against paper
      
      #rock agaisnt rock
          
    #scissors against scissors
      
# CORRECT BELOW HERE    

import random 

def evaluate(user_choice, computer_choice):

    if user_choice == computer_choice:
        #draw
        return "It's a draw!"

    elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice ==0:
        #computer wins
        return "You lose!"

    else: 
        # user wins
        return "You win!"

    # ask user to type rock paper or scissors
    
user_choice = input("Make a choice between rock (0), paper (1), scissors (2):")

    # make random choise among rock paper or sciussors


computer_choice = random.randint(0,2)

rps = ["rock","paper","scissor"]

print("You chose", rps[user_choice], "I choose", rps[computer_choice])

    # evaluate choices to find winner
print(evaluate(user_choice, computer_choice))

    # print results 