from data import MENU
from data import resources
import random

# TODO : 1. Print Report
# TODO : 2. Check resources sufficient
# TODO : 3. Process coins
# TODO : 4. Check transaction is successful

profit = 0.0


def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"money: {profit}")




command = input("What would you like? (espresso/latte/cappuccino): ").lower()
