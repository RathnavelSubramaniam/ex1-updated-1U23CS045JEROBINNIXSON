def oddoreve(x):
    if x % 2 == 1:
        return "odd number"
    if x % 2 == 0:
        return "Even number"
a = int(input("enter nubers only:"))
print(oddoreve(a))