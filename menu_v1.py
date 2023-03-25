"""Menu v1 First version of menu module"""
value_ = [["Beef burger", 5.69],
          ["Fries", 1.00],
          ["Fizzy drink", 1.00]
         ]
cheezy_ = [
           ["Cheeseburger", 6.69],
           ["Fries", 1.00],
           ["Fizzy drink", 1.00]
          ]
super_ = [["Cheeseburger", 6.69],
          ["Fries", 1.00],
          ["Smoothies", 2.00]
         ]

# Print all food and prices off the value menu
print("Value: ")
for item in value_:
    print(f"Food: {item[1]}, Cost: {item[1]}")
print()

# Print all food and prices off the cheezy menu
print("Cheezy: ")
for item in cheezy_:
    print(f"Food: {item[1]}, Cost: {item[1]}")
print()

# Print all food and prices off the super menu
print("Super")
for item in super_:
    print(f"Food: {item[1]}, Cost: {item[1]}")