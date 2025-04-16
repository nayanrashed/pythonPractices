#RECURSION
#A function to calculate the factorial of a number
'''def factorial(n):
    temp = 1
    for i in range(1,n+1):
        temp=temp*i
    return temp
fact = factorial(5)
print(fact)'''

# Factorial-Recursive
# def factorial2(n):
#     if n==1:
#         return 1
#     return n*factorial2(n-1)
# print('Input a number: ')
# num=input()
# print(factorial2(int(num)))

#Reverse List-Recursive
list = [1,2,3,4]

def reverse_list_recursive(some_list):
    if len(some_list)==0:
        return[]
    return [some_list[-1]]+reverse_list_recursive(some_list[:-1])
# print(reverse_list_recursive(list))


#fibo-Recursive
def fibo_recursive(n):
    if n<=1:
        return n
    return fibo_recursive(n-1)+fibo_recursive(n-2)
    
print(fibo_recursive(4))