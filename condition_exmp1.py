number = int(input("Give a Number:",))
# if number>=0:
#     if number %2==0:
#        print(number,"is a positive and even number")
#     else:
#         print(number,"is a positive and odd number")
# else:
#     if number %2==0:
#         print(number, "is a negative and even number")
#     else:
#         print(number, "is a negative and odd number")

if number>=0 and number%2==0:
    print(number,"is a positive and even number")
elif number>=0 and number%2==1:
    print(number,"is a positive and odd number")
elif number <=0 and number %2==0:
    print(number, "is a negative and even number")
else:
    print(number, "is a negative and odd number")