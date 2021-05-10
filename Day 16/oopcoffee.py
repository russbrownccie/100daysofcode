from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mymenu = Menu()
mymaker = CoffeeMaker()
mymoney = MoneyMachine()

IsOn = True

while IsOn == True:
    myorder = input (f"What would you like to drink?: {mymenu.get_items()}")

    if myorder.lower() == "report":
        mymaker.report()
        mymoney.report()
    elif myorder.lower() == "off":
        IsOn = False
    else:
        mybeverage = mymenu.find_drink(myorder)

        if mymaker.is_resource_sufficient(mybeverage) == True:
            if mymoney.make_payment(mybeverage.cost) == True:
                mymaker.make_coffee(mybeverage)

