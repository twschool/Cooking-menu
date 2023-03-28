"""Search combo's v1 First version of search combos module"""
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
while True:
    search_string = input(f"Search: ").title()
    try:
        search_result = menu[search_string]
        print(search_result)
        for item in search_result.items():
            print(f"Item: {item[0]} Price: {item[1]}")
    except KeyError:
        print("Key error")
