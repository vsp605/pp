import math
x, y = map(float, input("Enter the coordinates of the center of the circle (x, y): ").split())
r = float(input("Enter the radius of the circle: "))
x1, y1 = map(float, input("Enter the coordinates of the point (x1, y1): ").split())
distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
if distance < r:
    print("The point is inside the circle.")
elif distance == r:
    print("The point is on the circle.")
else:
    print("The point is outside the circle.")
