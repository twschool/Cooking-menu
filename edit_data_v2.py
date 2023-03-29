"""First version of the edit data module which
will let the user edit a combo"""

# This is imported for testing purposes and will be different in the final program
from delete_meals_function import delete_menu
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

all_combos = ""
for combo_name in menu:
    all_combos = f"{all_combos}\n{combo_name}"


def edit_data():
    error = ""
    global menu
    while True:
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
            dict_edit = menu[edit_combo]
        except KeyError:
            error = "Invalid input (Not a valid combo name)\n"
            continue
        
        enterbox_values = [edit_combo]
        enterbox_fields = []
        print(dict_edit)
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
        print(f"Output: {output}")
        error = ""
        print(f"Before function: {menu}")        
        delete_output = delete_menu(menu, edit_combo)[1]
        print(f"Delete output: {delete_output}")

        if delete_output[0] is True:
            menu = delete_output[1]
        else:
            print(f"Delete output error: {delete_output}")
            print("Error when deleting item")
        combo_name = output.pop(0)
        dict_to_add = list_to_dict(output)
        menu[combo_name] = dict_to_add
        print(f"After function: {menu}")


# Main routine
print(edit_data())
