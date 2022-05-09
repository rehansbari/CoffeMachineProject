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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
## How to access elements within a dictionary print(MENU['cappuccino']['ingredients']['water'])
## print(MENU['cappuccino']['cost'])

#function that generates report of how much resources are available including profit.
def print_report():
    print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${profit}")

#function that will deduct the resources available after the user has selected their drink of choice and inserted enough change
def make_coffee(coffee_type):
    coffee_water_amount = MENU[coffee_type]['ingredients']['water']
    coffee_grounds_amount = MENU[coffee_type]['ingredients']['coffee']
    if coffee_type != "espresso":
        coffee_milk_amount = MENU[coffee_type]['ingredients']["milk"]
        resources['water'] -= coffee_water_amount
        resources['milk'] -= coffee_milk_amount
        resources['coffee'] -= coffee_grounds_amount
    else:
        resources['water'] -= coffee_water_amount
        resources['coffee'] -= coffee_grounds_amount

    global profit
    profit += MENU[coffee_type]['cost']

#function which checks if the coffee machine has enough available resources to make the beverage
def check_resources(coffee_type):
    coffee_water_amount = MENU[coffee_type]['ingredients']['water']
    #coffee_milk_amount = MENU[coffee_type]['ingredients']["milk"]
    coffee_grounds_amount = MENU[coffee_type]['ingredients']['coffee']

    if coffee_water_amount > resources['water']:
        print("Sorry there is not enough water")
        return False
    elif coffee_type != "espresso" and MENU[coffee_type]['ingredients']["milk"] > resources['milk']:
        print("Sorry there is not enough milk")
        return False
    elif coffee_grounds_amount > resources['coffee']:
        print("Sorry there is not enough coffee grounds")
        return False
    else:
        return True

#Function to verify if the user has inserted enough change to acquire their desired beverage
def verify_transaction(change, coffee_type):
    cost_of_coffee = MENU[coffee_type]['cost']
    difference = round(change - cost_of_coffee, 2)
    if change >= cost_of_coffee:
        print(f"Here is ${difference} in change")
        print(f"Here is your {coffee_type}. Enjoy!")
        return True
    elif change < cost_of_coffee:
        print(f"Sorry, a {coffee_type} costs ${cost_of_coffee}. You inserted ${change}. Please try again.")
        return False

#Function to calculate how much change the user has inserted into the coffee machine
def process_coins():
    QUARTER = 0.25
    DIME = 0.10
    NICKEL = 0.05
    PENNY = 0.01

    print("Please insert coins.")
    user_quarters = int(input("how many quarters? "))
    user_dimes = int(input("how many dimes? "))
    user_nickels = int(input("how many nickels? "))
    user_pennies = int(input("how many pennies? "))
    user_total = (QUARTER * user_quarters) + (DIME * user_dimes) + (NICKEL * user_nickels) + (PENNY * user_pennies)
    return(user_total)

#Main method where the coffee machine gets started
def coffee_machine():
    user_coffee_choice = ""
    while user_coffee_choice != "off":
        user_coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_coffee_choice == "report":
            print_report()
        elif user_coffee_choice == "espresso" or user_coffee_choice == "latte" or user_coffee_choice == "cappuccino":
            if check_resources(user_coffee_choice):
                print("Success")
                inserted_change = process_coins()
                if(verify_transaction(inserted_change, user_coffee_choice)):
                    make_coffee(user_coffee_choice)

coffee_machine()
print("Goodbye!")
