year=int(input("Year: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year," is a Leap Year")
        else:
            print(year," is not a Leap year ")
    else:
        print(year," is a Leap Year")
else:
    print(year," is not a Leap year ")

# if year % 4 !=0:
#      print(year," is not a Leap year")
# elif year % 100 !=0:
#      print(year," is a Leap year")
# elif year % 400 !=0:
#      print(year," is not a Leap year")
# else:
#      print(year," is a Leap year")

