#author Sila2000
#It is a code which is intended to continuously prompt the user for integer input, add the integers to a list, and calculate the sum of the integers entered.
#And, it shows the integer list if user wants to see.

num_list = []
sum_num = 0

i = 0
while True:
    user_input = int(input(f"num[{i+1}] = "))
    num_list.append(user_input)

    checker = input("Do you want to continue?(0/1): ")
    print("O for exit and 1 to continue")
    if checker == '0':
        if len(num_list) == 1:
            print("Please enter at least two integers. Try again!")
            exit()
        else:
            sum_num += num_list[i]
            print(f"Sum = {sum_num}")
            know_num = input("Do you want list of number you have entered?(0/1): ")
            if know_num == '0':
                exit()
            elif know_num == '1':
                print(num_list)
                exit()
            else:
                print('''Entered Character Invalid. 
                You have to work hard. 
                Please scroll down to know your input nums.
                Thankyou!''')
                exit()
    elif checker == '1':
        sum_num += num_list[i]
        i += 1
    else:
        print("Entered Character Invalid. Please try again!")
