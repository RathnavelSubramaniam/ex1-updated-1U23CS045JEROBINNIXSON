#without function
a = float(input("Enter the float value:"))
b = float(input("Enter the float value:"))
a,b = b,a
print("after swapping a value:",a)
print("after swapping b value:",b)

#with function
def swap():
    a = int(input("Enter the float value:"))
    b = int(input("Enter the float value:"))
    a,b = b,a
    return a,b
print("After swapping:",swap())