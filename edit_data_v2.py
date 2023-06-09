"""Second version of the edit data module which
will let the user edit a combo (testing all of the different functions)"""

# This is imported for testing purposes and will be different in the final program
from delete_meals_v3 import delete_menu
from list_to_dict_funtion import list_to_dict
import easygui as eg

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


def edit_data():
    global menu

    error = ""
    

    while True:
        all_combos = ""
        for combo_name in menu:
            all_combos = f"{all_combos}\n{combo_name.title()}"
        enterbox_values = []
        enterbox_fields = []
        # Get the user input on what combo they would like to edit
        try:
            edit_combo = eg.enterbox(f"{error}All combo names: {all_combos}\nWhat combo would you like to edit?").title()
        except AttributeError:
            # error = "Invalid input (Input not submitted)\n"
            return [False]
            # Returns back to the main menu when I have that coded
        try:
            # Defines the dictionary we are about to let the user edit
            dict_edit = menu[edit_combo]
        except KeyError:
            error = "Invalid input (Not a valid combo name)\n"
            continue
        
        enterbox_values = [edit_combo]
        enterbox_fields = []
        enterbox_fields.append("Combo name")
        for item in dict_edit.items():
            """Add the existing values to the enterbox so the values
            are filled in automatically and can be easily edited"""
            enterbox_values.append(item[0])
            enterbox_values.append(item[1])
            # Add the enterbox fields in
            current_index = list(dict_edit.items()).index(item)
            enterbox_fields.append(f"Item {current_index}")
            enterbox_fields.append(f"Item {current_index} price")
    
        output = eg.multenterbox(msg=f"Here is the values of the {edit_combo} combo", fields=enterbox_fields, values=enterbox_values)
        
        error = ""
        delete_success, menu = delete_menu(menu, edit_combo)

        # If the deletion worked then        
        if delete_success is True:
            combo_name = output.pop(0).title()
            dict_to_add = list_to_dict(output)
            menu[combo_name] = dict_to_add
            print(f"Delete success\nNew menu: {menu}")
        else:
            print("Error when deleting item")


# Main routine
edit_data()