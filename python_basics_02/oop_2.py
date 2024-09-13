

class StoryBook:
    # CLASS VARIABLE
    no_of_books = 0
    discount = 0.3
    
    def __init__(self, name,price, author_name, author_birth,no_of_pages):
        #Setting instance variable
        self.name=name
        self.price=price
        self.author_name = author_name
        self.author_birth = author_birth
        self.publishing_year=2021
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books +=1
        
    # creating regular methods: 
    def get_book_info(self):
        print(f'The book name: {self.name}, price: {self.price}, pages:{self.no_of_pages}')
        
    def get_author_info(self):
        print(f'The author name: {self.author_name}, Born: {self.author_birth}')
    
    # Applying Discount to an Instance
    def apply_discount(self):
        self.price=int(self.price-self.price*self.discount)
    
    # METHOD TO CHANGE PRICE
    def set_price(self,new_price):
        self.price=new_price
    
    #CLASS METHOD 01
    @classmethod
    def set_discount(cls, new_discount):
        cls.discount=new_discount
    
    #CLASS METHOD 02
    @classmethod
    def construct_from_string(cls,book_string):
        name,price,author_name,author_birth,pages = book_string.split(',')
        return cls(name,price,author_name,author_birth,pages)
    
    #STATIC METHOD
    @staticmethod
    def is_new(publishing_year):
        if publishing_year>2020:
            print('Yes it is a New Book')
        else:
            print('Not new but Old is Gold')
    
        
 #Creating an instance/object of the StoryBook       
book_1= StoryBook('Hamlet',450,'Shakespears',1564,500)
book_2=StoryBook('Kite Runner',550, 'Khaled Hosasini',1965,220)



'''print(book_2.price)
book_2.set_price(1500)
print(book_2.price)'''

# Class method 01
'''print(book_1.price)
print(book_1.discount)
StoryBook.set_discount(0.6)
book_1.apply_discount()
print(book_1.price)'''

# Class Method 02
book_str = 'Harry Potter,1250,JK Rowling,1970,452'
harry_potter=StoryBook.construct_from_string(book_str)
print(harry_potter.name)

#Static Method
StoryBook.is_new(book_1.publishing_year)



