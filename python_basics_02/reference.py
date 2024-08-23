'''a=[1,2,3,4]
b=a
b[1]=5
print(a)'''



import copy as cp

def f(s_list):
    s_list.append('ok')

x=[1,2,3]
s=cp.copy(x)
f(s)
print(x)
print(s)