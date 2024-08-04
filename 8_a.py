x1, y1 = map(float, input("Enter the coordinates of the first point (x1, y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of the second point (x2, y2): ").split())
x3, y3 = map(float, input("Enter the coordinates of the third point (x3, y3): ").split())
area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
if area == 0:
    print("The points are collinear.")
else:
    print("The points are not collinear.")
