from menu import menu, resources

flag = "True"

resources_check = {}

def coffeemachine(choice):
    print("Please insert coins.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))
    payed = round(((quarters * 25) + (dimes * 10) + (nickles * 5) + pennies) / 100, 1)

    change = round(payed - menu[choice]['cost'], 1)

    if payed < menu[choice]['cost']:
        print("Please pay full money.")
    else:
        print(f"Here is ${change}.\nHere is your {choice} . Enjoy!")

def resource(choice1):
    # resources check
    water_check = resources['water'] - menu[choice1]['ingredients']['water']
    milk_check = resources['milk'] - menu[choice1]['ingredients']['milk']
    coffee_check = resources['coffee'] - menu[choice1]['ingredients']['coffee']

    key = ['water_check', 'milk_check', 'coffee_check']
    values = [water_check, milk_check, coffee_check]

    for i in range(0, 3):
        resources_check[key[i]] = values[i]

    if resources_check['water_check'] < menu[choice1]['ingredients']['water']:
        global  w
        w = 'water'
        return 'False'
    elif resources_check['milk_check'] < menu[choice1]['ingredients']['milk']:
        w = 'milk'
        return 'False'
    elif resources_check['coffee_check'] < menu[choice1]['ingredients']['coffee']:
        w = 'coffee'
        return 'False'
    else:
        return "True"


choice0 = input("What would you like? (espresso/latte/cappuccino) : ").lower()
while flag == "True":
    coffeemachine(choice0)
    if input("Do you wanna exit? yes/no ").lower() == "no":
        choice1 = input("What would you like? (espresso/latte/cappuccino) : ").lower()
        flag = resource(choice1)
        if flag == "True":
            choice0 = choice1
        else:
            print(f"Sorry there is not enough {w}. Please fill it !")
    else:
        flag = "False"



