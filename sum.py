#withoout function
x = 10
y = 20
sum = x + y
print("Sum of two numbers:",sum)

#with function
def add():
    x = int(input("Enter numbers only:"))
    y = int(input("Enter numbers only:"))
    sum = x + y
    return sum
print("Sum of two numbersL:",add())