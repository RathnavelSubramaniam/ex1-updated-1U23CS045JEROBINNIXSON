def prime(num):
    if num ==1:
        return "prime number"
    for i in range(2,num):
        if num % i == 0:
            return "Not prime number"
            break
        else:
            return "Prime number"
print(prime(3))