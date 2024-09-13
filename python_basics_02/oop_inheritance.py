class Robot:
    def __init__(self,name,version):
        self.name = name
        self.version= version
    
    def move_forward(self):
        print(f'{self.name} is moving forward')
    def move_backward(self):
        print(f'{self.name} is moving backward')
    def move_right(self):
        print(f'{self.name} is moving right')
    def move_left(self):
        print(f'{self.name} is moving left')
        
'''class HouseBot(Robot):
    pass'''
    
class HouseBot(Robot):
    def __init__(self, name, version, area_covered):
        super().__init__(name, version)
        self.area_covered=area_covered
    
    def clean(self):
        if self.area_covered>0:
            print(f'{self.name} is cleaning the house')
            self.area_covered -=30
            if self.area_covered<0:
                self.area_covered=0
        else:
            print('Cannot clean: Plz reset')
    
    def set_cover_area(self,area):
        if self.area_covered ==0:
            self.area_covered=area
        else:
            print('I can clean MORE area')
            
    #Method OverWriting
    def move_forward(self):
        print('moving forward from HouseBot Class')
        super().move_forward()

'''hBot = HouseBot('HB',2.5,30)
print(hBot.name)
hBot.move_forward() '''

houseBot = HouseBot('Rob',101,50)

print(houseBot.name)
houseBot.clean()
houseBot.clean()
houseBot.clean()
houseBot.move_forward()
print(houseBot.area_covered)
houseBot.set_cover_area(80)
houseBot.clean()