import easygui as eg

"""Code 'Borrowed' from the add_meals function to be used for
testing purposes in the edit data v2 (Not a actual component)"""
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