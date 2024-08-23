#list
'''fav_movie=[]
while True:
    print('Movie No '+ str(len(fav_movie)+1) +'or press enter to stop adding the list.')
    movie=input()
    if movie =='':
        break
    fav_movie=fav_movie+[movie]
    
if len(fav_movie)!=0:
    print('The Favorite Movies are:')
    for i in range(len(fav_movie)):
        print(fav_movie[i])'''

# in and not in
"""my_gear = ['ipad','android', 'laptop', 'camera', 'pc']
print('Enter item name:')
name=input()
if name in my_gear:
    print(name+" is in my tech list")
else:
    print('Not in my list')"""

#Assuming multiple value at Once
chocolate_milk_shake = ['choco','milk', 'ice cream', 'blending']
x,y,z,q=chocolate_milk_shake
print(x,y,z)

#strings are immutable form of list, that is they cannot be changed, while lists can be modified 