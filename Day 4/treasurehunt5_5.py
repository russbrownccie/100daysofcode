# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️","⬜️","⬜️"]
row4 = ["⬜️","⬜️","⬜️","⬜️","⬜️"]
row5 = ["⬜️","⬜️","⬜️","⬜️","⬜️"]

map = [row1, row2, row3, row4, row5]
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = (int(position[0])) -1
row = (int(position[1])) -1

map [row][column] = "X"




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
