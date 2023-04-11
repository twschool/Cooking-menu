import easygui as eg

output = eg.multenterbox(msg="Enter stuff", fields=["Name", "Address"])
print(f"Result: {output}")
print(output[1])