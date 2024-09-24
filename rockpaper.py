import random
rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
player_choice = int(input())
if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print("Please choose correct option")
print("Computer Chose:")
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if player_choice == computer_choice:
    print("It's a Tie")
elif player_choice == 0 and computer_choice == 2:
    print("You Win!")
elif player_choice == 2 and computer_choice == 1:
    print("You Win!")
elif player_choice == 1 and computer_choice == 0:
    print("You Win!")
else:
    print("Computer Wins!")
