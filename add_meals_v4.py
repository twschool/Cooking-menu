"""Add meals v4 fourth version of add meals component. This component splits up the
function into two seperate functions so it can be reused better"""
import easygui as eg

# Dictionary of menus with their respective items and prices
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


def list_to_dict(list_input):
    # The first item in the combo list is assumed to be the name of the combo and is popped off
            combo_name = list_input_list.pop(0)
            sorted_combo = []
            # Create a sorted list of combo items
            for i in range(0, len(list_input), 2):
                sorted_combo.append([list_input[i], list_input[i+1]])
            # Create a dictionary of combo items
            new_combo_dictionary = {}
            for meal in sorted_combo:
                new_combo_dictionary[meal[0]] = meal[1]
            return new_combo_dictionary, combo_name


def add_meals():
    try:
        # Asks the user how many items they want to add, if not entered the default will be 3
        how_many = int(eg.enterbox(msg="How many items do you want to add?\nPress enter for default of 3"))
    except ValueError:
        how_many = 3

    # Asks the user to enter the combo details
    msg = "Please enter information for you new combo"
    title = "Combo data entry"
    fields_ = ["Enter combo name"]
    for field_index in range(1, (how_many + 1)):
        fields_.append(f"Item {field_index} name:")
        fields_.append(f"Item {field_index} price:")
    # Multi-input box to collect information on the combo from the user
    raw_combo_list = eg.multenterbox(fields=fields_, msg="Enter combo information")
    
    # If the user presses cancel, raw_combo_list will be None
    if raw_combo_list is None:
        print("Add combo abandoned")
        # Return a list with a single element (False) to indicate that the addition of the combo was not successful
        return [False]
    else:
        # If the user presses OK, the list will contain the entered values. 
        # Now the user is asked to confirm the values
        msg_ = "Press OK if you are happy with these values or press cancel to abandon adding this list"
        raw_combo_list = eg.multenterbox(fields=fields_, msg=msg_, values=raw_combo_list)
        print(f"Raw combo list: {raw_combo_list}")
        if raw_combo_list is None:
            print("Add combo abandoned")
            return [False]
        else:
            
            # Return a list with 3 elements (True, dictionary of combo items, combo name) to indicate that the addition of the combo was successful
            return [True, new_combo_dictionary, combo_name.title()]


# Main routine
new_dict = add_meals(menu)
if new_dict[0] is True:
    menu[new_dict[2]] = new_dict[1]

# Print the updated menu
print(menu)
