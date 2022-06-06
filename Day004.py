import random

from sqlalchemy import between

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Papaer or 2 for Scissors\n"))

if player_choice >= 0 and player_choice < 3:
    print(game_images[player_choice])

    computer_choice = random.randint(0, 2)
    
    print("\n\nComputer chose:\n")
    print(game_images[computer_choice])

    if player_choice == computer_choice:
        print("It's a draw!")
    elif player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 1 and computer_choice == 0:
        print("You win!")
    elif player_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You lose!")
else:
    print("You chose wrong number!")