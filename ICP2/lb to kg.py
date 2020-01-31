pounds = []

n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    weight = int(input())

    pounds.append(weight)

print(pounds)
value= 2.2
kg = []
for x in pounds:
    kg.append(x / value)
print("The weights in kilograms is",kg)
