"""
Final version v3.

Now is tidier and complies with PEP8
"""

# All needed libraries imported
import easygui as eg

# Menu variable defined
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


# All functions defined

# Add meals function to prompt the user to add a meal and confirm their choice
def add_meals():
    """UI for adding meal to the menu dictionary"""
    global menu
    title_ = "Add meals menu"
    try:
        # Asks the user how many items they want to add, if not entered the default will be 3
        how_many = int(eg.enterbox(msg="How many items do you want to add?\nPress enter for default of 3", title=title_))
        if how_many <= 0:
            raise ValueError
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
    raw_combo_list = eg.multenterbox(fields=fields_, msg="Enter combo information", title=title_)

    # If the user presses cancel, raw_combo_list will be None
    if raw_combo_list is None:
        print("Add combo abandoned")
        # Return a list with a single element (False) to indicate that the addition of the combo was not successful
        return [False]
    else:
        # If the user presses OK, the list will contain the entered values. 
        # Now the user is asked to confirm the values
        msg_ = "Press OK if you are happy with these values or press cancel to abandon adding this list"
        raw_combo_list = eg.multenterbox(fields=fields_, msg=msg_, values=raw_combo_list, title=title_)
        empty_strings = 0

        for item in raw_combo_list:
            if item == '':
                empty_strings += 1
        if empty_strings >= 1:
            return [False, "Empty string not allowed"]
        elif raw_combo_list is None:
            return [False, "Add combo abandoned"]
        else:
            # The first item in the combo list is assumed to be the name of the combo and is popped off
            combo_name = raw_combo_list.pop(0)
            sorted_combo = []
            # Create a sorted list of combo items
            for i in range(0, len(raw_combo_list), 2):
                sorted_combo.append([raw_combo_list[i], raw_combo_list[i + 1]])
            # Create a dictionary of combo items
            new_combo_dictionary = {}
            for meal in sorted_combo:
                new_combo_dictionary[meal[0]] = meal[1]
            # Return a list with 3 elements (True, dictionary of combo items, combo name) to indicate that the addition of the combo was successful
            return [True, new_combo_dictionary, combo_name.title()]


def all_combo_names(is_string):
    """
    Returns a list of all combo names in the menu dictionary.
    """
    global menu
    if is_string:
        combo_string = ""
        for item in menu:
            combo_string = f"{combo_string}{item[0]}\n"
        return combo_string
    if not is_string:
        combo_list = []
        for item in menu:
            combo_list.append(item)
        return combo_list


def search_combo(search_string):
    """Searches for a combo in the menu dictionary."""
    global menu
    try:
        search_result = menu[search_string]
        return search_result
    except KeyError:
        return "Invalid"


def delete_menu(combo_input):
    """Deletes a combo from the menu dictionary."""
    global menu
    try:
        del menu[combo_input.title()]
        return True
    except KeyError:
        return False


def display_menu(menu_, combo_input):
    """Displays the details of a combo in the menu dictionary."""
    searched_item = menu_[combo_input]
    full_string = ""
    for item in searched_item.items():
        try:
            full_string = f"{full_string}\n{item[0]}   \t ${float(item[1]):.2f}"
        except ValueError:
            full_string = f"{full_string}\n{item[0]}   \t $No Data"
    return full_string


def edit_data():
    """Edits an existing combo in the menu dictionary."""
    global menu

    error = ""
    while True:
        combo_list = all_combo_names(is_string=False)
        enterbox_values = []
        enterbox_fields = []

        try:
            edit_combo = eg.buttonbox(f"{error}What combo would you like to edit?",
                                       choices=combo_list, title="Edit menu")
        except AttributeError:
            error = "Invalid input (Input not submitted)\n"
            continue
        try:
            dict_edit = menu[edit_combo]
        except KeyError:
            error = "Invalid input (Not a valid combo name)\n"
            continue

        enterbox_values = [edit_combo]
        enterbox_fields = []
        enterbox_fields.append("Combo name")
        for item in dict_edit.items():
            enterbox_values.append(item[0])
            enterbox_values.append(item[1])
            current_index = list(dict_edit.items()).index(item)
            enterbox_fields.append(f"Item {current_index}")
            enterbox_fields.append(f"Item {current_index} price")

        output = eg.multenterbox(msg=f"Here is the values of the {edit_combo} combo",
                                   fields=enterbox_fields, values=enterbox_values)
        if len(output) == len(enterbox_values):
            print("Success")
            print(f"Len output: {len(output)}\nLen Enterbox: {len(enterbox_values)}")
            print(output)
            print(enterbox_values)
        else:
            print(f"Len output: {len(output)}\nLen Enterbox: {len(enterbox_values)}")
        error = ""
        delete_success = delete_menu(edit_combo)

        if delete_success is True:
            combo_name = output.pop(0).title()
            dict_to_add = list_to_dict(output)
            menu[combo_name] = dict_to_add
            return [True, dict_to_add, edit_combo]
        else:
            return [False, "Error when deleting item"]


def list_to_dict(raw_combo_list):    
    if raw_combo_list is None:
        print("No raw combo list?")
        return [False]
    else:
        # The first item in the combo list is assumed to be the name of the combo and is popped off
        # combo_name = raw_combo_list.pop(0)
        sorted_combo = []
        # Create a sorted list of combo items
        for i in range(0, len(raw_combo_list), 2):
            sorted_combo.append([raw_combo_list[i], raw_combo_list[i+1]])
        # Create a dictionary of combo items
        new_combo_dictionary = {}
        for meal in sorted_combo:
            new_combo_dictionary[meal[0]] = meal[1]
    return new_combo_dictionary

while True:
    options = ["View menu", "Edit menu", "Exit"]
    message = "Choose an option"
    title_ = "Main menu"
    option_chosen = eg.buttonbox(choices=options, msg=message, title=title_)
    if option_chosen == "View menu":
        options = ["Display menu", "Search combo"]
        title_ = "View menu"
        option_chosen = eg.buttonbox(choices=options, title=title_, msg=message)
        
        if option_chosen == "Display menu":
            display_string = ""
            for item in menu.items():
                display_output = display_menu(menu, item[0])
                display_string = f"{display_string}\n\n{item[0]}: {display_output}"
            eg.msgbox(msg=display_string, title="Display menu")
        
        elif option_chosen == "Search combo":
            title_ = "Search menu"
            combo_list = all_combo_names(is_string=False)
            msg_ = "Which combo do you want to display"
            to_search = eg.buttonbox(choices=combo_list, msg=msg_, title=title_)
            search_result = search_combo(to_search)
            search_string = ""
            for item, price in search_result.items():
                search_string += f"Item: {item}  \t Price: {price}\n"
            eg.msgbox(msg=f"Search result:\n {search_string}", title=title_)
    
    elif option_chosen == "Edit menu":
        title_ = "Edit submenu"
        options = ["Delete combo", "Edit menu", "Add combo"]
        option_chosen = eg.buttonbox(choices=options, title=title_, msg=message)

        if option_chosen == "Delete combo":
            combo_list = all_combo_names(is_string=False)
            msg_ = "Which combo do you want to delete"
            to_delete = eg.buttonbox(choices=combo_list, msg=msg_, title="Delete menu")
            delete_menu(to_delete)

        elif option_chosen == "Edit menu":
            edit_data()

        elif option_chosen == "Add combo":
            adding_output = add_meals()
            if adding_output[0] is False:
                msg_ = f"Error: {adding_output[1]}"
                eg.msgbox(msg=msg_, title="Error")
            else:
                menu[adding_output[2]] = adding_output[1]

    elif option_chosen == "Exit":
        exit("Program exited")

    else:
        print("This should never execute")
