# Coffee Machine Simulation

# Resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# Menu with prices
menu = {
    "espresso": {
        "price": 1.50,
        "ingredients": {
            "water": 50,
            "coffee": 18
        }
    },
    "latte": {
        "price": 2.50,
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        }
    },
    "cappuccino": {
        "price": 3.00,
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        }
    }
}

def check_resources(coffee):
    #Check if resources are sufficient for the requested coffee.
    for ingredient in menu[coffee]["ingredients"]:
        if resources[ingredient] < menu[coffee]["ingredients"][ingredient]:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True

def process_coins():
    #Calculate total amount of coins inserted.
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies

def make_coffee(coffee):
    #Deduct resources and make coffee.
    for ingredient in menu[coffee]["ingredients"]:
        resources[ingredient] -= menu[coffee]["ingredients"][ingredient]
    print(f"Here is your {coffee}. Enjoy!")

def coffee_machine():
    #Main function to run the coffee machine.
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        
        if choice == "off":
            print("Turning off the coffee machine.")
            break
        elif choice in menu:
            if check_resources(choice):
                payment = process_coins()
                if payment >= menu[choice]["price"]:
                    change = round(payment - menu[choice]["price"], 2)
                    if change > 0:
                        print(f"Here is your change: ${change}")
                    make_coffee(choice)
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Invalid choice. Please try again.")


