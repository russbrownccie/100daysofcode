MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0
machine_on = True


def adjust_resources(user_choice):
    global money
    resources['water'] -= MENU[user_choice]['ingredients']['water']
    resources['milk'] -= MENU[user_choice]['ingredients']['milk']
    resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
    money += MENU[user_choice]['cost']
    return resources, money


def process_coins(user_choice):
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_coins = quarters * .25 + dimes * .1 + nickles * .05 + pennies * 0.01
    if total_coins >= float(MENU[user_choice]['cost']):
        change_back = round(total_coins - float(MENU[user_choice]['cost']), 2)
        if change_back > 0:
            print(f"Here is ${change_back} in change")
        print(f"Here is your {user_choice} ☕ - enjoy!")
        adjust_resources(user_choice)
    else:
        print("Sorry that's not enough money.  Money Refunded")


def verify_resources(user_choice):
    global resources, MENU
    if resources['water'] >= MENU[user_choice]['ingredients']['water']:
        if resources['milk'] >= MENU[user_choice]['ingredients']['milk']:
            if resources['coffee'] >= MENU[user_choice]['ingredients']['coffee']:
                process_coins(user_choice)

            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough milk")
    else:
        print("Sorry there is not enough water")


while machine_on:
    drink_made = False
    choice = input("What would you like?  (espresso/latte/cappuccino): ")
    if choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\nMoney:$ {money}")
    elif choice == "off":
        machine_on = False
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        verify_resources(choice)
    elif choice == 'refill':
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    else:
        print("Sorry that is not a valid choice")
