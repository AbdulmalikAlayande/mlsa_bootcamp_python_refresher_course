class LibraryItem: #this explains or shows the parent class that set itself as the blue print that the object attribute is created on 
    def __init__(self,title,author,publication_year):  #this initialize the LibraryItem and give the object attributes such as title, author and publication_year
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    def __str__(self):    #Returns a formatted string representation of the LibraryItem, showing its title, author and publication_year .
        return f"[Title:{self.title}, Author:{self.author}, Publication year:{self.publication_year}]"

class Book(LibraryItem):    #this explains or shows the child class Book that set itself with the attribute of the parent class LibraryItem
    def __init__(self,title,author,publication_year,genre,isbn):     #this initialize the Book and give the object attributes such as title, author, publication_yea,genre and isbn
        super().__init__(title,author,publication_year)     #the super(), allows access to the methods and attributes of the parent class (LibraryItem) in a child class (Book) 
        self.genre = genre
        self.isbn = isbn
        
    def __str__(self):            #Returns a formatted string representation of the LibraryItem, showing its title, author, publication_year, genre and isbn.
        return f"[Title:{self.title}, Author:{self.author}, Publication year:{self.publication_year}, Genre:{self.genre}, ISBN:{self.isbn}, Available to be taken: Yes]"
    
class Journal(LibraryItem):                     #this explains or shows the child class journal that set itself with the attribute of the parent class LibraryItem
    def __init__(self,title,author,publication_year,volume,issue):      #this initialize the Book and give the object attributes such as title, author, publication_yea,volume and issue
         super().__init__(title,author,publication_year)            #the super(), allows access to the methods and attributes of the parent class (LibraryItem) in a child class (journal) 
         self.volume = volume
         self.issue =issue
         
    def __str__(self):            #Returns a formatted string representation of the LibraryItem, showing its title, author, publication_year, volume and issue.
        return f"[Title:{self.title}, Author:{self.author}, Publication year:{self.publication_year}, Volume:{self.volume}, Issue:{self.issue}, Available to be taken: Yes]"

class Magazine(LibraryItem):                #this explains or shows the child class magazine that set itself with the attribute of the parent class LibraryItem
    def __init__(self,title,author,publication_year,issue_month,editor):                 #this initialize the Book and give the object attributes such as title, author, publication_year,issue_month and editor
        super().__init__(title,author,publication_year)                     #the super(), allows access to the methods and attributes of the parent class (LibraryItem) in a child class (magazine)
        self.issue_month = issue_month
        self.editor = editor
        
    def __str__(self):                   #Returns a formatted string representation of the LibraryItem, showing its title, author, publication_year, issue_month and edition.
        return f"[Title:{self.title}, Author:{self.author}, Publication year:{self.publication_year}, Issue month:{self.issue_month}, Editor:{self.editor}, Available to be taken: Yes]"

class ReferenceBook(Book):                  #this explains or shows the child class ReferenceBook that set itself with the attribute of the parent class Book( this took the attribute of the book)
    def __init__(self,title,author,publication_year,genre,isbn,reference_section):      #this initialize the ReferenceBook and give the object attributes such as title, author, publication_yea,genre, isbn and reference_section
        super().__init__(title,author,publication_year,genre,isbn)                      #the super(), allows access to the methods and attributes of the parent class (Book) in a child class (ReferenceBook)
        self.reference_section = reference_section
        
    def __str__(self):                      #Returns a formatted string representation of the Book, showing its title, author, publication_year, genre, isbn and reference_section.
         return f"[Title:{self.title}, Author:{self.author}, Publication year:{self.publication_year}, Genre:{self.genre}, ISBN:{self.isbn}, Reference section:{self.reference_section}, Available to be taken: NO]"
    
# Creating instances for the derived class and printing details
book = Book("To The top","Chidi Emmanuel",1994,"Motivation",1233445556)
journal = Journal("Iron Wall","Ademola benson",2019,2,3)
magazine = Magazine("Who Wants to Be A Millionaira","Iheajamatu Anthony",2024,"November","Oshin Ayobami")
referencebook = ReferenceBook("Acquring your Golden Streams","Moh Sheriff",1980,"Motivation",2346355,"Section B") 

# Printing the details of each derived class
print(book)
print(journal)
print(magazine)
print(referencebook)