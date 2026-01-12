#19
numbers = []
while True:
    num = int(input("Enter a number"))
    if num == 0:
        break
    numbers.append(num)
print("Sum of the numbers is:", sum(numbers))
