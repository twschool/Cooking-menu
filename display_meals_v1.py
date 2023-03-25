"""Display meals v1 First version of display meals module"""
# Dictionary to store all of the Menu data
menu = {
    "Value": {
        "Beef burger": 5.69,
        "Fries": 1.00,
        "Fizzy drink": 1.00
    },
    "Cheezy": {
        "Cheeseburger": 6.69,
        "Fries": 1.00,
        "Fizzy drink": 1.00
    },
    "Super": {
        "Cheeseburger": 6.69,
        "Fries": 1.00,
        "Smoothies": 2.00
    }
}
"""Iterating through all of the menu items printing 
the Menu name then all of the items and their prices"""
while True:
    input_combo = input("What combo do you want to display: ")
    found = False
    for menu_name, menu_items in menu.items():
        if menu_name.lower() == input_combo.lower():
            found = True
            print(f"{menu_name}:")
            for food, price in menu_items.items():
                print(f"{food}: {price}")
            print()
    if found is False:
        print("No menu of that found")  