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
    for item in dict_edit.items():
        enterbox_values.append(item)
        enterbox_values.append(dict_edit[item])

        
