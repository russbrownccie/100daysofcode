import random
from replit import clear
from art import logo



def calculate_score(cards):
  """Take a list of cards and return score from the cards"""
  if sum(cards)==21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) >21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, Opponent has blackjack"
  elif user_score == 0:
    return "Player win with a Blackjack"
  elif user_score > 21:
    return "You went over - you lose"
  elif computer_score > 21:
    return "Opponent went over - you win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You Lose"


def play_game():
  print(logo)
  user_cards = [deal_card(), deal_card()]
  computer_cards = [deal_card(), deal_card()]
  is_game_over = False


  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print (f"   Your cards: {user_cards}, current score: {user_score}\n   Dealer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Would you like to take another card press 'y' or 'n'")
      if user_should_deal == "y":
        user_cards.append(deal_card())
        calculate_score(user_cards)
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print (f"   Your final hand: {user_cards}, final score: {user_score}")
  print (f"   Dealer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack?  Type 'y' or 'n': ") == "y":
  clear()
  play_game()

