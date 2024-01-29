#tetration or hyper-4 operation.
#example: 2^(2^2) = 2^4 = 16
#here number of 2 is 3 which is considered as the height.

def hyper4(a, b):
    a_ori = a
    if b >= 0:
        if b == 0:
            return 1
        else:
            for i in range(0, b - 1):
                a = pow(a_ori, a)
            return a


a = int(input("Enter base = "))
b = int(input("Enter height = "))

print(f"hyper4({a},{b}) = ", hyper4(a,b))
    
