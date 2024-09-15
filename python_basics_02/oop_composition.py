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
        
    # regular method 1
    def get_book_info(self):
        print(f'The book name: {self.name}, price: {self.price}, pages:{self.no_of_pages}')
        
    # regular method 2
    def get_author_info(self):
        print(f'The author name: {self.author_name}, Born: {self.author_birth}')
       
    # Applying Discount to an Instance
    def apply_discount(self):
        self.price=int(self.price-self.price*self.discount)
    

class Library:
    def __init__(self, book_list=None):
        if book_list is None:
            self.book_list = []
        else:
            self.book_list =  book_list
            
    def get_all_books(self):
        for book in self.book_list:
            print(f'Title: {book.name}, Author: {book.author_name}, Price:{book.price}')   
    
    def add_book(self,book):
        self.book_list.append(book)
    
    def remove_book(self,book):
        self.book_list.remove(book)
    

     
#Creating an instance/object of the StoryBook       
book_1= StoryBook('Hamlet',450,'Shakespears',1564,500)
book_2=StoryBook('Kite Runner',550, 'Khaled Hosasini',1965,220)

p_library=Library()
p_library.add_book(book_1)
p_library.add_book(book_2)

p_library.get_all_books()

p_library.remove_book(book_2)

p_library.get_all_books()
