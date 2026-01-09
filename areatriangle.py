def area(base, height):
    area = 0.5 * base * height
    return area
a = int(input("enter base value:"))
b = int(input("enter height value:"))
print("Area of triangle:",area(a, b))