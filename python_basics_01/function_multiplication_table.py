# Making function
def multi_table(n):
    print(n,"x 1 =",n * 1)
    print(n,"x 2 =",n * 2)
    print(n,"x 3 =",n * 3)
    print(n,"x 4 =",n * 4)
    print(n,"x 5 =",n * 5)
    print(n,"x 6 =",n * 6)
    print(n,"x 7 =",n * 7)
    print(n,"x 8 =",n * 8)
    print(n,"x 9 =",n * 9)
    print(n,"x 10 =",n * 10)
    return

n = int(input("Enter a number:"))
# multi_table(n)
# multi_table(n+1)
for i in range(1, n+1):
    multi_table(i)
    print("-----")