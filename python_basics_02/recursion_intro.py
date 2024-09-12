#RECURSION
#A function to calculate the factorial of a number
'''def factorial(n):
    temp = 1
    for i in range(1,n+1):
        temp=temp*i
    return temp
fact = factorial(5)
print(fact)'''

def factorial2(n):
    if n==1:
        return 1
    return n*factorial2(n-1)
print('Input a number: ')
num=input()
print(factorial2(int(num)))
    
