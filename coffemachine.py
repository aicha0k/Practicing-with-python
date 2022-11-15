#print report TO SEE RESOURCES
#check if resources are enough
#process coins
#check if transaction successful
#make coffee and deduct resources
from menu import resources
from menu import MENU


def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def resources_sufficient(order, resources):
    if order == "espresso":
        if water >= 50 and coffee >= 18:
            return True
        else:
            return False
    elif order == "latte":
        if water >= 200 and milk >= 150 and coffee >= 24:
            return True
        else:
            return False
    elif order == "cappuccino":
        if water >= 250 and milk >= 100 and coffee >= 24:
            return True
        else:
            return False

def _order():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    coins = input("Please insert coins. ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if order == "espresso":
        if total >= 1.5:
            change = total - 1.5
            if resources_sufficient(order, resources) == True:
                make_coffee(order)
                print(f"Here is ${change} in change.")
                print(f"Here is your {order}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
            
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif order == "latte":
        if total >= 2.5:
            change = total - 2.5
            if resources_sufficient(order, resources) == True:
                make_coffee(order)
                print(f"Here is ${change} in change.")
                print(f"Here is your {order}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
            
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif order == "cappuccino":
        if total >= 3.0:
            change = total - 3.0
            if resources_sufficient(order, resources) == True:
                make_coffee(order)
                print(f"Here is ${change} in change.")
                print(f"Here is your {order}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
            
        else:
            print("Sorry that's not enough money. Money refunded.")
        


def make_coffee(their_order):



