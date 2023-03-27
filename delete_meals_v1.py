"""Delete combo's v1 First version of delete combos module"""
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

def delete_menu(menu_, combo_input_):
    try:
        menu_.pop(combo_input_.title())
        return [True, menu_]
    except KeyError:
        return [False]

while True:
    deletion_input = input("Menu to delete: ")
    delete_output = delete_menu(menu, deletion_input)
    if delete_output[0] is False:
        print("Invalid input")
    else:
        menu = delete_output[1]
    print(f"Fixed menu: {menu}")