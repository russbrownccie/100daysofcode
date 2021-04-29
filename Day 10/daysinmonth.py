def is_leap(leapyear):
  if leapyear % 4 == 0:
    if leapyear % 100 == 0:
      if leapyear % 400 == 0:
        yearisleap = True
      else:
        yearisleap = False
    else:
      yearisleap = True
  else:
    yearisleap = False
  return yearisleap



def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year):
    month_days[1] = 29
    return month_days[month - 1]
  else:
    return month_days[month - 1]
  

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


