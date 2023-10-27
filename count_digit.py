#author Sila2000
def count(number):
    if number == 0:
        return 1
    else:
        count_digit = 0
        while number > 0:
            rem = number % 10
            count_digit += 1
            number //= 10
        return count_digit


print("Counting Digit")
num = int(input("Enter an integer: "))

if num < 0:
    print(f"Number of digits in {num} = {count(-num)}")
else:
    print(f"Number of digits in {num} = {count(num)}")
