#Recursion

def factorial(n):
    fact = 1
    for i in range(1,n+1):
           fact = fact*i
    return fact

print(factorial(4))

def factorial (n):
    if n <= 1 :
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))