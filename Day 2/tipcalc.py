#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print ("Welcome to the tip calculator")
totalbill = float(input("What was the total bill? $"))
percentage = int(input ("What percentage tip would you like to give? 10, 12, or 15? "))
actualpercentage = percentage / 100
finalbill = totalbill + totalbill * actualpercentage
people = int(input("how many people to split the bill? "))
perperson = round(finalbill/people, 2)
print(f"Each person should pay: ${perperson}")

