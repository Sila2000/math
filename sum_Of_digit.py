#author Sila2000
print("Sum of digits in number (Non-negative Integer):")
num = o_num = int(input("Enter number: "))

sum_digit = 0

while num > 0:
    rem = num % 10
    sum_digit += rem
    num //= 10

print(f"Sum of digits in {o_num} = {sum_digit}")
