elements = [10, 20, 30, 40, 50]
print(" List:", elements)
item = int(input("Enter the element to insert: "))
position = int(input("Enter the position (index): "))
elements.insert(position, item)
print("Updated List:", elements)
