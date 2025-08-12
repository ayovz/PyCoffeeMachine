import os

from data import MENU, resources, ascii_art
import random

# TODO : 1. Print Report
# TODO : 2. Check resources sufficient
# TODO : 3. Process coins
# TODO : 4. Check transaction is successful

profit = 0.0


def print_report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"money: $ {profit}")


def items_check(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry. Not enough ingredients.")
            return False
    return True


def process_coins():
    print("Please enter coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def successful_transaction(money_received, drink_price):
    if money_received >= drink_price:
        change = round(money_received - drink_price, 2)
        if change > 0:
            print(f"Here's your change ${change}.")
        global profit
        profit += drink_price
        return True
    else:
        print("Sorry. Not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}! Enjoy☕!")


def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')


is_on = True

while is_on:
    print(ascii_art)
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if command == "off":
        is_on = False
    elif command == "report":
        print_report()
    elif command in MENU:
        drink = MENU[command]
        if items_check(drink["ingredients"]):
            payment = process_coins()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(command.capitalize(), drink["ingredients"])
    else:
        print("Sorry, I don't understand that command.")

    clear_screen()
