#author Sila2000
print("Product of digits in number (Non-negtive integer):")
num = o_num = int(input("Enter number: "))

mult_digit = 1

while num > 0:
    rem = num % 10
    mult_digit *= rem
    num //= 10

print(f"Sum of digits in {o_num} = {mult_digit}")
