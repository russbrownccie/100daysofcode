# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
print(names_string)
names = names_string.split(", ")
print(names)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
total = (len(names) - 1)

payer=random.randint(0, total)
payername = names[payer]
print(payername + " is going to buy the meal today!")
# could comment out all of the above and use the one below instead
# print((random.choice(names)) + " is going to buy the meal today!")
