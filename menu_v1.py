value_ = [["Beef buger", 5.69], ["Fries", 1.00], ["Fizzy drink"]]
cheezy_ = [["Cheeseburger", 6.69], ["Fries", 1.00], ["Fizzy drink", 1.00]]
super_ = [["Cheeseburger", 6.69], ["Fries", 1.00], ["Smoothies", 2.00]]
menu = [value_, cheezy_, super_]
for item in menu:
    print(f"Food: {item[1]}, Cost: {item[1]}")