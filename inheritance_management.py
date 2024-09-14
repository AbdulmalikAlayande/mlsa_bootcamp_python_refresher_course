class LibraryItem:
    def __init__ (self,title,author,publication_year):
        self._title =title
        self._author = author
        self._publication_year = publication_year

    def __str__(self):
        return f"""
        [
        title: {self._title},
        author:{self._author},
        publication_year:{self._publication_year}
        ]
        """
    
class Book(LibraryItem):
    def __init__ (self, fields,isbn):
        #super().__init__(title,author,publication_year)
        self.fields=fields
        self.isbn =isbn
    def __str__(self):
        return f"""
        [
            fields = {self.fields}
            isbn = {self.isbn}
        ]
        """
    #def get_title(self):
        #return self._title
    #def set_title(self):
        #self.title= title 

class Journal(LibraryItem):
    def __init__(self, volume,issue):
        #super().__init__(title,author,publication_year)
        self.volume = volume
        self.issue  = issue

    def __str__(self):
        return f"""
        [
        volume: {self.volume}
        issue: {self.issue}
        ]
        """

class Magazine(LibraryItem):
    def __init__(self,issue_month,editor):
        self.issue_month = issue_month
        self.editor = editor

    def __str__(self):
        return f"""
        issue month: {self.issue_month}
        editor :{self.editor}
        """
class Reference_book(Book): #reference_book is inheriting from the subclass "book" which demonstrates multilevel inheritance
    def __init__(self,reference_section):
        self.reference_section = reference_section
       
    def __str__(self):
        return f"""
        [
        reference section = {self.reference_section}
        
        ]
        """

    def borrow_book(self, borrower_name):
        print(f"Sorry {borrower_name}, this book cannot be borrowed")


my_book = Book("romance","CA83U0888")
print(my_book)
my_journal = Journal("volume3", "issue 9320")
print(my_journal)
my_magazine = Magazine("june","NYC fashion")
print(my_magazine)
my_reference_book = Reference_book("EIJTHG8RWNF0")
print(my_reference_book)
print(my_reference_book.borrow_book("michael"))