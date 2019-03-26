"""
CP1404/CP5632 - Practical - Suggested Solution
Shop calculator program to determine total (discounted) price
"""

Sum = 0
value = int(input("Enter number of items: "))
while value < 0:
    print("Invalid number of items!")
    value = int(input("Enter number of items: "))
for i in range(value):
    price = float(input("Enter Price of item: "))
    Sum += price

if Sum > 100:
    Sum *= 0.9

print("Total price for {} items is ${:.2f}".format(value, Sum))
