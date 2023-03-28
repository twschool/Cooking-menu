"""First version of the edit data module which
will let the user edit a combo"""

import easygui as eg
error = ""
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

while True:
    enterbox_values = []
    enterbox_fields = []
    # Get the user input on what combo they would like to edit
    try:
        edit_combo = eg.enterbox(f"{error}All combo names: {all_combos}\nWhat combo would you like to edit?").title()
    except AttributeError:
        error = "Invalid input (Input not submitted)\n"
        continue
        # Restarts the loop
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
    if output == dict_edit:
        print("Same")
    print(f"Output: {output}")
    error = ""
