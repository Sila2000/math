def absolute_func(num):
    if num >= 0:
        return num
    else:
        return -num


user_input = input("Enter the number: ")

try:
    user_num = int(user_input)
    print(f"Absolute value of {user_num} = {absolute_func(user_num)}")
except ValueError:
    try:
        user_num = float(user_input)
        print(f"Absolute value of {user_num} = {absolute_func(user_num)}")
    except ValueError:
        print("Entered character is neither an integer nor a float")
