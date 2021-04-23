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

import random
print("Welcome to the Rock Paper Scissors Championship Trainer")
player = int(input("Choose your weapon! - Type 0 for Rock, 1 for Paper, 2 for Scissors\n\n"))
computer = random.randint(0,2)

if player == 0:
  print(rock)
elif player == 1:
  print(paper)
else:
  print(scissors)

print ("Computer chooses:\n")
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
else:
  print(scissors)

if player == 0 and computer == 1:
  print("You lose - Paper beats Rock")
elif player == 0 and computer == 2:
  print("You win - Rock beats Scissors")
elif player == 1 and computer == 0:
  print("You win - Paper beats Rock")
elif player == 1 and computer == 2:
  print("You lose - Scissors beats Paper")
elif player == 2 and computer == 0:
  print("You lose - Rock beats Scissors")
elif player == 2 and computer == 1:
  print("You win - Scissors beats Paper")
else:
  print("It's a tie")
