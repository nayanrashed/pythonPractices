"""def sum(a,b):
    return a+b
a = sum(2,5)
print(a)
"""
#fibonacci series
def fibonacci(n):
    if n==0:
        return 0
    else:
        x=0
        y=1
        print(x,end=",")
        print(y,end=",")
        for i in range(1,n):
            z=x+y
            x=y
            y=z
            print(z,end=',')
fibonacci(8)