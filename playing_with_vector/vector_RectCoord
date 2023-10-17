print("Vector in Rectangular Coordinate System")

coord_listA = []
x_A = float(input("Enter x_A: "))
coord_listA.insert(0, x_A)
y_A = float(input("Enter y_A: "))
coord_listA.insert(1, y_A)
z_A = float(input("Enter z_A: "))
coord_listA.insert(2, z_A)
print("Coordinates of A: ", coord_listA)

coord_listB = []
x_B = float(input("Enter x_B: "))
coord_listB.insert(0, x_B)
y_B = float(input("Enter y_B: "))
coord_listB.insert(1, y_B)
z_B = float(input("Enter z_B: "))
coord_listB.insert(2, z_B)
print("Coordinates of B: ", coord_listB)

diff_x = x_A - x_B
diff_y = y_A - y_B
diff_z = z_A - z_B
vector = []
print("\nChoose initial and final points:")
init_point = input("Enter initial point: ").upper()
fin_point = input("Enter final point: ").upper()

if init_point == 'A' and fin_point == 'B':
    vector.insert(0, -diff_x)
    vector.insert(1, -diff_y)
    vector.insert(2, -diff_z)
    print(f"Vector from {init_point} to {fin_point} = {vector}")
elif init_point == 'B' and fin_point == 'A':
    vector.insert(0, diff_x)
    vector.insert(1, diff_y)
    vector.insert(2, diff_z)
    print(f"Vector from {init_point} to {fin_point} = {vector}")
else:
    print("\033[1mInvalid Entry. Please try again!")
