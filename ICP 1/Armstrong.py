n = int(input("Enter a number: "))
sum = 0
m = n
while m > 0:
   number = m % 10
   sum += number ** 3
   m //= 10
if n == sum:
   print("Is an Armstrong number")
else:
   print("Is not an Armstrong number")