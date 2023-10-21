#author Sila2000
import math

init_coord_list = []
x_i = float(input("Enter x_i: "))
init_coord_list.insert(0, x_i)
y_i = float(input("Enter y_i: "))
init_coord_list.insert(1, y_i)
z_i = float(input("Enter z_i: "))
init_coord_list.insert(2, z_i)
print("Coordinates of initial point: ", init_coord_list)

fin_coord_list = []
x_f = float(input("Enter x_f: "))
fin_coord_list.insert(0, x_f)
y_f = float(input("Enter y_f: "))
fin_coord_list.insert(1, y_f)
z_f = float(input("Enter z_f: "))
fin_coord_list.insert(2, z_f)
print("Coordinates of B: ", fin_coord_list)

diff_x = x_f - x_i
diff_y = y_f - y_i
diff_z = z_f - z_i

print("Magnitude of the vector: ", math.sqrt(pow(diff_x, 2) + pow(diff_y, 2) + pow(diff_z, 2)))
