from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
morebidders = True
listofbidders={}

while morebidders == True:
  bidder = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  listofbidders [bidder] = bid
  otherbidders = input("Are there any other bidders? Type 'yes' or 'no'")
  if otherbidders == "yes":
    clear()
  else:
    morebidders = False


topbid = 0
for key in listofbidders:
  if (listofbidders[key]) > topbid:
    winner = key
    topbid = listofbidders[key]

clear()
print(f"The winner is {winner} with a bid of ${topbid}.")
