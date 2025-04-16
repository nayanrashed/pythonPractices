identity = {'Name':'Sabbir', 'Age':'21', 'Job':'Student'}

#Printing values
for i in identity.values():
    print(i)
    
#Printing keys
for i in identity.keys():
    print(i)
    
#Printing keys+values
for i in identity.items():
    print(i)

# X=list(identity.keys())
# Y=list(identity.values())
# print(X)
# print(Y)
# print(type(identity.keys()))

'''# A HANDY TRICK
for k,v in identity.items():
    print('key: '+k+' value: '+v)
'''
# use of 'in' keyword
'''print('Name' in identity)
print('name' in identity)
print('nayan' in identity.values())
print('Age' in identity.keys())'''

# the get() method
'''print(str(identity.get('Name', 'Default')))
print(str(identity.get('Height', 'Default')))'''


# set default
# print(identity.setdefault('Name', 'Cosmos'))
# print(identity.setdefault('Height','6ft'))
# print(identity)
