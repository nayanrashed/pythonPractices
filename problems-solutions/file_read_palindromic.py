f = open('number.txt','w+')
f.write('12344321')
f.close()

f = open('number.txt','r+')
some_list = list(f.read())
f.close()

is_palindromic = True
for i in range(int(len(some_list)/2)):
    if some_list[i] != some_list[len(some_list)-i-1]:
        is_palindromic=False

if is_palindromic:
    f=open('number.txt','a')
    f.write('Yes')
else:
    f = open('number.txt','w')
    for i in range(len(some_list)):
        f.write('0')