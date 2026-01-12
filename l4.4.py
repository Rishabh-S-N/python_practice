num = list(range(1, 101))
even_num = []
odd_num = []
for num in num:
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)
print("Even Numbers:", even_num)
print("Odd Numbers:", odd_num)
