#author Sila2000
print("Factorial")
num = int(input("Enter a non-negative integer: "))

if num == 0:
    print(f"{num}! = 1")
else:
    mult = 1
    for i in range(1, num+1):
        mult *= i
    print(f"{num}! = {mult}")
