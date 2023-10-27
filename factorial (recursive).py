#author Sila2000

def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n*factorial(n - 1)


print("Factorial Calculator:")
num = int(input("\nEnter a non-negative integer: "))
if num < 0:
    print('''Please enter a non-negative integer.
0, 1, 2, and so on comes under the category of non-negative integers.''')
else:
    print(f"{num}! = {factorial(num)}")
