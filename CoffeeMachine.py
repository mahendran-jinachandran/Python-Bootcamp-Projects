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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}ml")
    print(f"Money: {profit}₹")

def is_resource_sufficient(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item] > resources[item]:
            print(f"Sorry, these is no sufficient {item}")
            return False
    
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):

    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} 375. Enjoy!")

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if(user_input == "off"):
        break

    elif(user_input == "report"):
        print_report()
    
    elif(user_input == "espresso" or user_input == "latte" or user_input == "cappuccino"):

        ordered_item = MENU[user_input]
        if not is_resource_sufficient(ordered_item["ingredients"]):
            continue

        user_paid_amount = process_coins()
        if is_transaction_successful(user_paid_amount, ordered_item["cost"]):
            make_coffee(user_input, ordered_item["ingredients"])
    else:
        print("Wrong input. Choose the correct one.")
        