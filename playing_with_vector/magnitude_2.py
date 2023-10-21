#author Sila2000
import math

print("Enter the components of the vector:")
x_comp = float(input("Enter the component along x-axis: "))
y_comp = float(input("Enter the component along y-axis: "))
z_comp = float(input("Enter the component along z-axis: "))

mag_vector = math.sqrt(pow(x_comp, 2) + pow(y_comp, 2) + pow(z_comp, 2))
print(f"\nThe magnitude of the vector = {mag_vector}")
