class Point2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return f'Point2D({self.x,self.y})'
    
    def __str__(self):
        return f'Class: Point2D, x:{self.x}, y:{self.y}'
    
    def __add__(self,other):
        if isinstance(self, other.__class__):
            return Point2D(self.x + other.x, self.y + other.y)
        else:
            return None
        
    def __sub__(self,other):
        if isinstance(self, other.__class__):
            return Point2D(self.x - other.x, self.y - other.y)
        else:
            return None
        
    def __eq__(self,other):
        if isinstance(self, other.__class__):
            return self.x == other.x and self.y==other.y
        
    def __ne__(self,other):
        if isinstance(self, other.__class__):
            return self.x != other.x and self.y != other.y  
        
    def __lt__(self,other):
        if isinstance(self, other.__class__):
            return self.x<other.x or (self.x==other.x and self.y<other.y)
    
    def __hash__(self):
        return hash(self.x+self.y)
    
p1=Point2D(1,2)
p2=Point2D(3,4)
p3=Point2D(1,2)
'''print(p1)
print(repr(p1))
print(str(p1))'''
# print(p1+p2)
# print(p1-p2)
'''print(p1==p2)
print(p1 is p2)
print(p1==p3)'''

'''print(p1 != p2)
print(p1 < p2)'''

point_set=set()
point_dict=dict()

point_set.add(p1)
print(point_set)

point_dict[p1] = str(p1)
print(point_dict)