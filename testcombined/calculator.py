print(f"==================Area Calculator 📐==================")

whichshape = int(input("Which shape do you want to calculate the area of? 1) Triangle2) Rectangle3) Square4) Circle5) Quit\n"))
if whichshape == 1:
    height = float(input("Enter the height of the triangle: "))
    base = float(input("Enter the base of the triangle: "))
    area = (height * base) / 2
    print(f"The area of the triangle is: {area}")
elif whichshape == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area1 = length * width
    print(f"The area of the rectangle is: {area1}")
elif whichshape == 3:
    side = float(input("Enter the side of the square: "))
    area2 = side * side
    print(f"The area of the square is: {area2}")
elif whichshape == 4:
    radius = float(input("Enter the radius of the circle: "))
    area3 = 3.14 * radius * radius
    print(f"The area of the circle is: {area3}")
elif whichshape == 5:
    print("Goodbye!")