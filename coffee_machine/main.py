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


money = 0


machine_off = False

while not machine_off:
    
    
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    
    # calculates and updates the values of resources dict
    
    def espresso():
        resource_espresso_water = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resource_espresso_coffee = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        resources["water"] = resource_espresso_water
        resources["coffee"] = resource_espresso_coffee
        return resources
    
    def latte():
        resource_latte_water = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resource_latte_milk = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resource_latte_coffee = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["water"] = resource_latte_water
        resources["coffee"] = resource_latte_coffee
        resources["milk"] = resource_latte_milk
        return resources
    
    
    
    def cappuccino():
        resource_cappuccino_water = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resource_cappuccino_milk = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resource_cappuccino_coffee = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        resources["water"] = resource_cappuccino_water
        resources["coffee"] = resource_cappuccino_coffee
        resources["milk"] = resource_cappuccino_milk
        return resources
    
    
    
    
    if choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            espresso()
        
    elif choice == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            latte()
    elif choice == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]: 
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            cappuccino()
    elif choice == "report":
        print(f"Water : {resources['water']}")
        print(f"milk : {resources['milk']}")
        print(f"coffee : {resources['coffee']}")
    elif choice == "off":
        machine_off = True
    else:
        print("Please provide correct input!")

