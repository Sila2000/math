#author Sila2000
import math

print("Quadratic Equation Solver")
a = float(input("Enter the numerical coefficient of the quadratic term: "))
b = float(input("Enter the numerical coefficient of the linear term: "))
c = float(input("Enter the constant term: "))

if a == 0:
    print("\nThe equation is not quadratic. It is a linear equation.")
    answer = input("Do you the answer of this quadratic equation? ").upper()
    if answer == 'Y':
        print(f"Answer = {-c/b}")
    else:
        print("Ok!")

else:
    D = pow(b, 2) - (4*a*c)
    if D > 0:
        print("\nRoots of the equation are real and different.")
        print(f"Roots are {(-b + math.sqrt(D))/(2*a)} and {(-b - math.sqrt(D))/(2*a)}")
    elif D == 0:
        print(f"\nRoots of the equation are real and same.\rRoot is {-b/(2*a)}")
    else:
        print(f"\nRoots are imaginary.")
        print(f"Roots are {(-b/(2*a))} + i {(math.sqrt(-D))/(2*a)} and {(-b/(2*a))} - i {(math.sqrt(-D))/(2*a)}")
