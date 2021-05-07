from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


mymenu = Menu()
mymachine = CoffeeMaker()
mymoney = MoneyMachine()
coffee_maker_on = True

while coffee_maker_on:

    print("What would you like to drink? :" + mymenu.get_items())
    order_name = input("Choice?: ").lower()

    if order_name == "report":
        mymachine.report()
        mymoney.report()
    elif order_name == "off":
        print("Turning off Coffeemaker")
        coffee_maker_on = False
    else:
        mydrink = mymenu.find_drink(order_name)
        print(mydrink)
        # if order_name == "latte":
        #     mydrink = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
        # elif order_name == "espresso":
        #     mydrink = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
        # else:
        #     mydrink = MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)

        if mymachine.is_resource_sufficient(mydrink):
            if mymoney.make_payment(mydrink.cost):
                mymachine.make_coffee(mydrink)
