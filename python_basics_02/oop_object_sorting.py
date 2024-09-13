class Toy:
    def __init__(self,name,price):
        self.name=name
        self.price = price
    def sort_priority(self):
        return self.price
    

def print_toy_objects(toy_list):
    for obj in toy_list:
        print(f'Toy:{obj.name}, Price: {obj.price}')
        
toy_1=Toy('Woody',1250)
toy_2=Toy('Train',850)
toy_3=Toy('Bus',750)
toy_4=Toy('Mandalorian',1850)

toys=[toy_1,toy_2,toy_3,toy_4]


# using sort() function
toys.sort(key=Toy.sort_priority)
# print_toy_objects(toys)

#using sorted() function
sorted_toys=sorted(toys, key=Toy.sort_priority)
# print_toy_objects(sorted_toys)

#lambda function(Arrow function)
'''result = lambda x,y,z:x+y+z'''

# USING LAMBDA FUNCTION with sort()
toys_again=[toy_1,toy_2,toy_3,toy_4]
toys_again.sort(key=lambda x: x.price)
print_toy_objects(toys_again)


# Using sorted()
sorted_toys_again = sorted(toys, key=lambda x:x.price)
print_toy_objects(sorted_toys_again)