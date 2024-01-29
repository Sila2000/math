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
b = int(input("Enter hyperexponent = "))

print(f"hyper4({a},{b}) = ", hyper4(a,b))
    
