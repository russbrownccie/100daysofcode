#Write your code below this line ๐
def prime_checker(number):
  IsPrime = True
  testrange = int(number / 2)
  for test in range (2, testrange):
    primetest = number % test
    if primetest == 0: 
      IsPrime = False
  if IsPrime:
    print ("It's a prime number.")
  else:
    print ("It's not a prime number.")




#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
