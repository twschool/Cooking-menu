"""Search combo's v2 Second version of search combos module"""
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

def search_combo(seach_string_):
    try:
        search_result = menu[search_string_]
        return search_result
    except KeyError:
        return ""


search_string = input("Search: ")
search_combo(search_string)
