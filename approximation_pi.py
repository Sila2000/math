def pi(n):
    approx_sum = 0
    for i in range(n):
        x = 4*pow(-1, i)/(2*i + 1)
        approx_sum += x
    return approx_sum


print("\033[1mApproximated Value of Pi\033[0m")
num = int(input("Enter the number of terms: "))
print(f"Approximated value of pi using {num} terms = {pi(num)}")
