#Number Guessing Game Objectives:

import random
from art import logo
print(logo)

computer_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
#print(f"psttt, the correct answer is {computer_number}")

#This function sets the difficulty and sets the number of guesses available variable
def difficulty():
  
  difficulty = input("Choose a difficulty.  Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
      return 10
  elif difficulty == "hard":
      return 5
  else:
      print("You didn't give me a valid option\nI will pick hard for you since you don't seem too smart")
      return 5

#This function will run after each incorrect guess to see if he won or lost

def has_player_lost():
  if guesses != 0:
    print("Guess again")
  else:
    print("You've run out of guesses - you lose")
    print(f"The number was {computer_number}") 
guesses = difficulty()


#This is the input and initial operations phase

while guesses > 0:
  print(f"You have {guesses} attempts remaining to guess the number")
  player_guess = int(input("Make a guess: "))

  if player_guess > computer_number:
    print("Too High")
    guesses -= 1
    has_player_lost()
  elif player_guess < computer_number:
    print("Too Low")
    guesses -= 1
    has_player_lost()
  else:
    guesses = 0
    print(f"You got it! - The Answer was {computer_number}")
