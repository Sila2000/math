#Sila2000
#it is a code intended to take non-negative integer from user and continuously add its digit unless
#single digit is achieved
#it will also show the number of steps the process has gone through and if user wants can get the list
#of results which appeared at every step.

sum_list = []

print("Continuous Sum:")
user_input = int(input("Enter a number = "))
sum_list.append(user_input)

count_step = 0
while True:
    sum_digit = 0

    while user_input > 0:
        rem = user_input % 10
        sum_digit += rem
        user_input //= 10

    sum_list.append(sum_digit)
    count_step += 1

    print(f"Step {count_step}:")

    if 0 < sum_digit < 10:
        print(f"Final Sum = {sum_digit}")

        want = input("Do you want the list of inputs? (0/1): ")
        if want == '0':
            print("Thankyou!")
            exit()
        elif want == '1':
            print(sum_list)
            exit()
        else:
            print("Entered Character Invalid.")
            exit()

    else:
        user_input = sum_digit
        print(f"Sum: {sum_digit}")
