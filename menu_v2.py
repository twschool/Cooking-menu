"""Menu v2 Second version of menu module, (Switched to using a dictionary)"""
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
for menu_name, menu_items in menu.items():
    print(f"{menu_name}:")
    for food, price in menu_items.items():
        print(f"{food}: {price}")
    print()
