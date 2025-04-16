# my_stuff = {'book':'Cookbook', 'phone':'OnePlus', 'Home':'Bangladesh'}
# print(my_stuff['book'])
# x={0:0, 1:100, 2:200}
# print(x[1])
# # Order in Dictionary 
# a=[1,2,3]
# b=[2,3,1]
# print(a==b)

# c = {1:10, 2:20}
# d ={ 2:20, 1:10}
# print(c==d)

# concatenation of dictionaries
D={'a':100,'b':200}
E={'c':300,'d':400}
new_dic=D.copy()
print(new_dic)
new_dic.update(E)
print(new_dic)