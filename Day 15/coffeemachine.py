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


def get_report(resources, money_in_machine):
    print("Water: " + str((resources["water"])) +"ml")
    print("Milk: " + str((resources["milk"])) +"ml")
    print("Coffee: " + str((resources["coffee"])) +"g")
    print(f"Money: ${money_in_machine}")


def get_money(drink, drink_cost):

    global money_in_machine
    beverage = drink
    quarters = .25
    dimes = .10
    nickles = .05
    pennies = .01
    print("Please insert coins")
    quarters_deposit = int(input("How many quarters?: "))
    dimes_deposit = int(input("How many dimes?:"))
    nickles_deposit = int(input("how many nickles?: "))
    pennies_deposit = int(input("how many pennies?: "))
    total_money = round((quarters_deposit * quarters) + (dimes_deposit * dimes) + (nickles_deposit * nickles) + (
                pennies_deposit * pennies), 2)
    print(total_money)
    if total_money < drink_cost:
        print("Sorry, that's not enough money.  Money refunded")
    else:
        change = round((total_money - drink_cost), 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {beverage}! ☕  Enjoy!")
        resources["water"] -= water_needed
        resources["milk"] -= milk_needed
        resources["coffee"] -= coffee_needed
        money_in_machine += drink_cost


def get_beverage(drink):

    global water_needed, milk_needed, coffee_needed, drink_cost, resources
    water_needed = MENU[drink]["ingredients"]["water"]
    milk_needed = MENU[drink]["ingredients"]["milk"]
    coffee_needed = MENU[drink]["ingredients"]["coffee"]
    drink_cost = MENU[drink]["cost"]
    if water_needed > resources["water"]:
        print("Sorry, there is not enough water")
    elif milk_needed > resources["milk"]:
        print("Sorry, there is not enough milk")
    elif coffee_needed > resources["coffee"]:
        print("Sorry, there is not enough coffee")
    else:
        get_money(drink, drink_cost)
        return water_needed, milk_needed, coffee_needed, drink_cost


coffee_machine_on = True
water_needed = 0
milk_needed = 0
coffee_needed = 0
drink_cost = 0
drink = ""
money_in_machine = 0.00
while coffee_machine_on:

    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "report":
        get_report(resources, money_in_machine)
    elif request == "off":
        print ("powering off coffee machine")
        coffee_machine_on = False
    elif request == "refill":
        print ("refilling the machine with more resources!")
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    else:
        get_beverage(request)
