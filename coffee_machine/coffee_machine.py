MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

COINS = {
    "quarter": .25,
    "dime": .1,
    "nickel": .05,
    "penny": .01
}

profit = 0

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 760
}

def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert your payment:")
    quarters = int(input("Insert any number of quarters: ")) * COINS["quarter"]
    dimes = int(input("Insert any number of dimes: ")) * COINS["dime"]
    nickels = int(input("Insert any number of nickels: ")) * COINS["nickel"]
    pennies = int(input("Insert any number of pennies: ")) * COINS["penny"]
    total = quarters + dimes + nickels + pennies
    return total

def transaction_complete(payment, cost):
    if payment > cost:
        change = round(payment - cost, 2)
        print(f"Here is your change: {change}")
        global profit
        profit += cost
        return True
    else:
        print("Please insert the correct amount of money!")
    return False

def make_drink(drink, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Thank you for you purchase! Here is your {drink}.")



is_on = True

while is_on:
    choice = input(f"""\n
                   What would you like? 
                   --------------------------
                   Latte: enter latte
                   Espresso: enter espresso
                   Cappuccino: enter cappuccino
                   Resource Report: enter report
                   Off: enter off\n""")

    if choice == "off":
        is_on =  False
    elif choice == "report":
        print(f"""
              Resource Report:
              ---------------------------
              Water: {resources['water']}
              Milk: {resources['milk']}
              Coffee: {resources['coffee']}
              Money: {profit}\n""")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction_complete(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])



    
