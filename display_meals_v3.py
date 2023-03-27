"""Display meals v3 Third version of display meals module"""
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

def display_menu(menu_, combo_input_):
    searched_item = menu_[combo_input_]
    full_string = ""
    for item in searched_item.items():
        print(item)
        full_string = f"{full_string}\n{item[0]}   \t ${item[1]:.2f}"
    return full_string


combo_input = input("What combo do you want to display: ").title()
display_output = display_menu(menu, combo_input)
print(display_output)