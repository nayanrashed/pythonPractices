'''#Open a file
f=open('a.txt','w')

# getting info from file
print('name = ', f.name)
print('is it closed? ', f.closed)
print('mode= ', f.mode)
f.write('I am writing from code using python.')
f.close()

# appending a file
f = open('a.txt','a')
f.write(' I also love JavaScript')
f.close()

# r+ mode
f = open('a.txt','r+')
info = f.read()
# info = f.read(10)
print(info)
f.close()'''

'''# w+ mode
f =open('a.txt','w+')
f.write('All data lost')
f.close()'''