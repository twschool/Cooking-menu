"""add meals v1 First version of add meals module"""
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


def add_meals(menu_):
    try:
        how_many = int(eg.enterbox(msg = "How many items do you want to add?\nPress enter for default of 3"))
    except ValueError():
        how_many = 3

    msg = "Please enter information for you new combo"
    title = "Combo data entry"
    fields_ = ["Enter combo name"]
    
    for field_index in range(1, (how_many + 1)):
        fields_.append(f"Item {field_index} name:") 
        fields_.append(f"Item {field_index} price:") 
    raw_combo_list = eg.multenterbox(fields=fields_, msg="Enter combo information")
    sorted_combo = []
    msg_ = "Press OK if you are happy with these values or press cancel to abandon adding this list"
    raw_combo_list = eg.multenterbox(fields=fields_,msg=msg_, values=raw_combo_list)
    if sorted_combo is None:
        print("Add combo abandoned")
        return [False]
    else:
        # Seperates the combo list to be a sorted list inside of a list so its easier to iterate through
        combo_name = raw_combo_list.pop(raw_combo_list[0])
        for i in range(0, len(raw_combo_list), 2):
            sorted_combo.append([raw_combo_list[i], raw_combo_list[i+1]])
        new_combo_dictionary = {}
        for meal in sorted_combo:
            new_combo_dictionary[meal[0]] = meal[1]
        return [True, new_combo_dictionary, combo_name.title()]

        
    print(sorted_combo)


# Main routine
new_dict = add_meals(menu)
if new_dict[0] is True:
    menu[new_dict[2]] = new_dict[1]

print(menu)