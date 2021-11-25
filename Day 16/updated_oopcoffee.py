from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
coffee_money = MoneyMachine()
machine_on = True



while machine_on:

    choice = input(f"What would you like to drink? {coffee_menu.get_items()}: ")
    if choice == "report":
        coffee_maker.report()
        coffee_money.report()
    elif choice == "off":
        machine_on = False
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
         coffee_chosen = (coffee_menu.find_drink(choice))
         if (coffee_maker.is_resource_sufficient(coffee_chosen)) == True:
            if coffee_money.make_payment(coffee_chosen.cost) == True:
                  coffee_maker.make_coffee(coffee_chosen)
    else:
        print("Sorry that is not a valid choice")
