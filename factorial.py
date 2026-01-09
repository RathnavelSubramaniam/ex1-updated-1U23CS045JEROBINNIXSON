def factorial(a):
    res = 1
    for i in range(a,1,-1):
        res *= i
    return res
print(factorial(4))