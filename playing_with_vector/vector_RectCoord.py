print("Vector in 3D Rectangular Coordinate System")

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
    if diff_x == 0.0:
        vector.insert(0, diff_x)
    else:
        vector.insert(0, -diff_x)
    if diff_y == 0.0:
        vector.insert(1, diff_y)
    else:
        vector.insert(1, -diff_y)
    if diff_z == 0.0:
        vector.insert(2, diff_z)
    else:
        vector.insert(2, -diff_z)
    print(f"Vector from {init_point} to {fin_point} = {vector}\n")

    ans = input("Do you want the unit vector notation of the vector? (Y/N) ").upper()
    if ans == 'Y':
        if diff_x != 0 and diff_y != 0 and diff_z != 0:
            print(f"Vector = ({-diff_x}\033[1mi\033[0m) + ({-diff_y}\033[1mj\033[0m) + ({-diff_z}\033[1mk\033[0m)")
        else:
            if diff_x == 0 and diff_y != 0 and diff_z != 0:
                print(f"Vector = ({-diff_y}\033[1mj\033[0m) + ({-diff_z}\033[1mk\033[0m)")
            elif diff_x != 0 and diff_y == 0 and diff_z != 0:
                print(f"Vector = ({-diff_x}\033[1mi\033[0m) + ({-diff_z}\033[1mk\033[0m)")
            elif diff_x != 0 and diff_y != 0 and diff_z == 0:
                print(f"Vector = ({-diff_x}\033[1mi\033[0m) + ({-diff_y}\033[1mj\033[0m)")
            elif diff_x == 0 and diff_y == 0 and diff_z != 0:
                print(f"Vector = {-diff_z}\033[1mk")
            elif diff_x == 0 and diff_y != 0 and diff_z == 0:
                print(f"Vector = {-diff_y}\033[1mj")
            elif diff_x != 0 and diff_y == 0 and diff_z == 0:
                print(f"Vector = {-diff_x}\033[1mi")
            elif diff_x == diff_y == diff_z == 0:
                print("Vector = \033[1m0")
    elif ans == 'N':
        exit()
    else:
        print("\0331mInvalid Entry. Try again!")

elif init_point == 'B' and fin_point == 'A':
    vector.insert(0, diff_x)
    vector.insert(1, diff_y)
    vector.insert(2, diff_z)
    print(f"Vector from {init_point} to {fin_point} = {vector}")

    ans = input("Do you want the unit vector notation of the vector? (Y/N) ").upper()
    if ans == 'Y':
        if diff_x != 0 and diff_y != 0 and diff_z != 0:
            print(f"Vector = ({diff_x}\033[1mi\033[0m) + ({diff_y}\033[1mj\033[0m) + ({diff_z}\033[1mk\033[0m)")
        else:
            if diff_x == 0 and diff_y != 0 and diff_z != 0:
                print(f"Vector = ({diff_y}\033[1mj\033[0m) + ({diff_z}\033[1mk\033[0m)")
            elif diff_x != 0 and diff_y == 0 and diff_z != 0:
                print(f"Vector = ({diff_x}\033[1mi\033[0m) + ({diff_z}\033[1mk\033[0m)")
            elif diff_x != 0 and diff_y != 0 and diff_z == 0:
                print(f"Vector = ({diff_x}\033[1mi\033[0m) + ({diff_y}\033[1mj\033[0m)")
            elif diff_x == 0 and diff_y == 0 and diff_z != 0:
                print(f"Vector = {diff_z}\033[1mk")
            elif diff_x == 0 and diff_y != 0 and diff_z == 0:
                print(f"Vector = {diff_y}\033[1mj")
            elif diff_x != 0 and diff_y == 0 and diff_z == 0:
                print(f"Vector = {diff_x}\033[1mi")
            elif diff_x == diff_y == diff_z == 0:
                print("Vector = \033[1m0")
    elif ans == 'N':
        exit()
    else:
        print("\033[1mInvalid Entry. Try again!")

else:
    print("\033[1mInvalid Entry. Please try again!")
