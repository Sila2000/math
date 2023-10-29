num_list = []
mult_num = 1

i = 0
while True:
    user_input = int(input(f"num[{i+1}] = "))
    num_list.append(user_input)

    checker = input("Do you want to continue?(0/1): ")
    print("O for exit and 1 to continue")
    if checker == '0':
        if len(num_list) == 1:
            print("please enter at least two integers")
            exit()
        else:
            mult_num *= num_list[i]
            print(f"Product = {mult_num}")
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
        mult_num *= num_list[i]
        i += 1
    else:
        print("Entered Character Invalid. Please try again!")
