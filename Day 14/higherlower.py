import random
from art import logo
from art import vs
from game_data import data
from replit import clear

dict_a = (random.choice(data))
dict_b = "a"
playerscore = 0
gamenotover = True
choice = "c"


def challenger():
    global dict_a
    global dict_b
    dict_b = (random.choice(data))
    while dict_b == dict_a:
        dict_b = (random.choice(data))
    return dict_b


def replacechampion(newchamp):
    global dict_a
    global dict_b
    dict_a = newchamp
    dict_b = (random.choice(data))
    while dict_b == dict_a:
        dict_b = (random.choice(data))
    return dict_b


def fightcard(champion, challenger):
    global choice
    champion_name = dict_a['name']
    champion_description = dict_a['description']
    champion_country = dict_a['country']
    challenger_name = dict_b['name']
    challenger_description = dict_b['description']
    challenger_country = dict_b['country']
    champion_followers = int(dict_a['follower_count'])
    challenger_followers = int(dict_b['follower_count'])

    print(
        f"Compare A: {champion_name}, a {champion_description} from {champion_country} with {champion_followers}."
    )
    print(vs)
    print(
        f"Against B: {challenger_name}, a {challenger_description} from {challenger_country} with {challenger_followers}."
    )
    choice = input("Who has more followers?  Type 'A' or 'B': ").lower()
    return choice


def score(score1, score2, playerscore,gamestatus):
    global choice
    if choice == "a":
        clear()
        print(logo)
        if score1 > score2:
            playerscore += 1
            print(f"You're right! Current Score {playerscore}.")

        else:
            print(f"Sorry, that's wrong. Final Score: {playerscore}")
            return gamenotover == False
    elif choice == "b":
        clear()
        print(logo)
        if score1 < score2:
            playerscore += 1
            print(f"You're right! Current Score {playerscore}.")

        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final Score: {playerscore}")
            return gamenotover == False

print (logo)
challenger()


while gamenotover == True:
    score1 = int(dict_a['follower_count'])
    score2 = int(dict_b['follower_count'])

    fightcard(dict_a, dict_b)

    if choice == "a":
      clear()
      print(logo)
      if score1 > score2:
        playerscore += 1
        print(f"You're right! Current Score {playerscore}.")
        replacechampion(dict_b)

      else:
        print(f"Sorry, that's wrong. Final Score: {playerscore}")
        gamenotover = False
    elif choice == "b":
        clear()
        print(logo)
        if score1 < score2:
          playerscore += 1
          print(f"You're right! Current Score {playerscore}.")
          replacechampion(dict_b)
        else:
          clear()
          print(logo)
          print(f"Sorry, that's wrong. Final Score: {playerscore}")
          gamenotover = False
