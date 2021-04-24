#Day 5 - Password Generator Project
#Note this password generator is Base58 - no 0, O, I, or l to avoid confusion with other similiar letters
import random
lowercaseletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercaseletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to the PyPassword Generator!")
nr_lowerletters= int(input("How many lower case letters would you like in your password?\n")) 
nr_upperletters= int(input("How many upper case letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for alpha in range(nr_lowerletters): 
  password.append(random.choice(lowercaseletters))
for upperalpha in range(nr_upperletters):
  password.append(random.choice(uppercaseletters))
for symbo in range(nr_symbols):
  password.append(random.choice(symbols))
for numero in range(nr_numbers):
  password.append(random.choice(numbers))

random.shuffle(password)

final_password = ("".join(password))
print(final_password)

