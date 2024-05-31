# Initialize recipes
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

# Initialize starting resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Function that prints out a report of remaining resources
def report(resources, profit):
    '''Takes in current resources and money and prints out a resource report.'''
    print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${profit}")

# Function that checks if resources are sufficient to for the selected recipe
def check_resource_sufficiency(drink, resources):
    '''Takes in requested drink and current resources and outputs if there is sufficient resources to complete recipe as a boolean
        as well as prints out what is missing.'''
    recipe = MENU[drink]['ingredients']
    for ingredient in recipe:
        if recipe[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

# Function to process coins
def process_coins( quarters, dimes, nickels, pennies):
    '''Takes in coins and processes them into a total amount that is returned'''
    money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return money

# Function that checks transaction is successful
def successful_transaction_check(drink, money, profit):
    '''Function that takes in drink ordered, money given and current profit and returns profit added from successful orders where there is enough money.
        If there's not enough money, no profit is added and change refunded'''
    # Find cost of drink
    cost = MENU[drink]['cost']
    # If money inputted is sufficient to cover cost, add money to profit and refund any change
    if money >= cost:
        success = True
        profit = profit + cost
        if money > cost:
            print(f"Here is ${format(money-cost, '.2f')} in change.")
    # Else return coints
    else:
        print("Sorry, that's not enough money. Money refunded.")
        success = False
    return profit, success

# Function to make the coffee
def make_coffee(drink, resources, profit, money):
    '''Function that takes in drink of choice, current resources, current profit and inputted money. It then checks if there is enough money to transact, 
        adding to the total profit'''
    # Check if enough money and resources - only add profit if both are sufficient
    stocked = check_resource_sufficiency(drink, resources)
    if stocked:
        profit, solvent = successful_transaction_check(drink, money, profit)
    else:
        solvent = False

    # Only make coffee if enough resources and deduct from remaining resources
    if solvent and stocked:
        recipe = MENU[drink]['ingredients']
        for ingredient in recipe:
            resources[ingredient] = resources[ingredient] - recipe[ingredient]
        print(f"Here is your {drink}. Enjoy!")

    return profit, resources


# Keep coffee machine on until 'off' is inputted and start with zero profit
machine_on = True
profit = 0
while machine_on:
    # Start up the coffee machine by asking user their drink preference
    option = ''
    while option not in ('espresso', 'latte', 'cappuccino', 'off', 'report'):
        option = input("What would you like? Espresso/latte/cappuccino/report/off? ").lower()

    # Coffee machine actions option selected
    if option == 'off':
        machine_on = False
    elif option == 'report':
        report(resources, profit)
    else:
        # Take in money - assumes integer input
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))

        money = process_coins( quarters, dimes, nickels, pennies)

        profit, resources = make_coffee(option, resources, profit, money)