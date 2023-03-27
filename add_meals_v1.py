"""add meals v1 First version of add meals module"""
import easygui as eg
menu_ = {
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

try:
    how_many = int(eg.enterbox(msg = "How many items do you want to add?\nPress enter for default of 3"))
except ValueError:
    how_many = 3

msg = "Please enter information for you new combo"
title = "Combo data entry"
fields_ = ["Enter combo name"]


for i in range(1, (how_many) + 1):
    fields_.append(f"Item {i} name")
    fields_.append(f"Item {i} price")

raw_combo_list = eg.multenterbox(fields=fields_, msg="Enter combo information")
combo_list = raw_combo_list
combo_name = combo_list[0]
combo_list.remove(combo_name)

# Seperates the combo list to be a sorted list inside of a list so its easier to iterate through
for i in range(0, len(combo_list), 2):
    sorted_combo.append([combo_list[i], combo_list[i+1]])


while True:
    done = eg.buttonbox(choices=["Yes", "No"])


print(sorted_combo)

if (fsf) {
    system.println("Hi")
}

