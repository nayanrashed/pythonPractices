import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



p_load = int(input("Point Load:" ))
a = int(input("distance a: "))
b = int(input("distance b: "))
l = a+b
r1 = (p_load*b)/l
r2 = (p_load*a)/l
print("Reaction R1: ",r1 )
print("Reaction R2: ",r2 )
a1= a+1
l1= l+1
li1=list(range(a1))
li2 = list(range(a,l1))
li = li1 + li2
m1=[]
for x in range(0,a1,1):
    m = r1*x
    m1.append(m)
for x in range(a,l1,1):
    m = r1*x-p_load*(x-a)
    m1.append(m)
print(li)
print(m1)

max_n = m1[0]
for n in m1:
    if n > max_n:
        max_n = n
print('Maximum Moment;', max_n)

plt.plot(li, m1)
plt.title("Moment Diagram")
plt.xlabel("Distance")
plt.ylabel("Moment")
plt.show()
