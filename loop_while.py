i=1
# while i<=10:
#     print(i)
#     i=i+1

def multi_table(n):
    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))
        
n = int(input("Enter a number(0 to exit):"))
while n!=0:
    multi_table(n)
    print("Done")
    n = int(input("Enter a number(0 to exit):"))