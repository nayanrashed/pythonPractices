''' 001
class StoryBook:
    pass

#Creating an instance/object of the StoryBook
book_1= StoryBook()
book_2=StoryBook()
# print(book_1)


#instance variable
book_1.name='Hamlet'
book_1.price=450
book_1.authorName='Shakspear'

book_2.name='the kite runner'
book_2.price=550
book_2.authorName='khaled Hosseini'

print(book_1.name)
print(book_2.name)'''

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
        
    # creating regular methods: 1
    def get_book_info(self):
        print(f'The book name: {self.name}, price: {self.price}, pages:{self.no_of_pages}')
        
    def get_author_info(self):
        print(f'The author name: {self.author_name}, Born: {self.author_birth}')
    
    # creating regular methods: 
    # Applying Discount to an Instance
    def apply_discount(self):
        self.price=int(self.price-self.price*self.discount)
    
        
 #Creating an instance/object of the StoryBook       
book_1= StoryBook('Hamlet',450,'Shakespears',1564,500)
book_2=StoryBook('Kite Runner',550, 'Khaled Hosasini',1965,220)

#book_1.name='Romio and Juliet'
# print(book_1.name)
# print(book_2.name)

# book_1.get_book_info()
# StoryBook.get_book_info(book_1)
# book_1.get_author_info()

# print(book_1.no_of_books)
# print(book_2.no_of_books)
# print(StoryBook.no_of_books)


print(book_2.price)
book_2.discount=0.5
book_2.apply_discount()
print(book_2.price)
