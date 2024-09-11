# library management system

#base class
class LibraryItem:

    # declaring object attributes
    
    def __init__(self,title, author, publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year


    # the library item should always display title

    def __str__(self):
        return self.title

# book, jornal , magazine classes showing inheritance

class Book(LibraryItem):


    #extending library item attributes

    def __init__(self,title, author, publication_year,genre,isbn):
        super(Book,self).__init__(title, author, publication_year)
        self.genre=genre
        self.isbn=isbn


    def __str__(self):
        return str({"Genre":self.genre, "ISBN":self.isbn})


    def borrow(self):
        if borrowed:
            print("not available")
        else:
            borrowed=True

    def returnbook(self):
        if borrowed:
            borrowed=false
        else:
            print("i dont think the bool belongs here")


class journal(LibraryItem):


    #extending library item attributes

    def __init__(self,title, author, publication_year,volume,issue):
        super(journal,self).__init__(title, author, publication_year)
        self.volume=volume
        self.issue=issue


    def __str__(self):
        return str({"title":self.title,"volume":self.volume, "Issue":self.issue})

    
        

class Magazine(LibraryItem):


    #extending library item attributes

    def __init__(self,title, author, publication_year,issue_month,editor):
        super(Magazine,self).__init__(title, author, publication_year)
        self.editor=editor
        self.issue_month=issue_month


    def __str__(self):
        return str({"title":self.title,"editor":self.editor, "Issue_month":self.issue_month})



class ReferenceBook(Book):
    
    def __init__(self,title, author, publication_year,genre,isbn,ref_sec):
        super(ReferenceBook,self).__init__(title, author, publication_year,genre,isbn)
        self.ref_sec=ref_sec



    def borrow(self):
        print("THIS BOOK CANNOT BE BORROWED")








# instantiating object
book1=Book("rich Dad, poor Dad","Ben Carson", "2010", "motivational", 11111111111)
journal1=journal("random", "daniel", 2021, 1, 12)
mag=Magazine("punch","punch writers guild",20224,"may","micheal")
ref=ReferenceBook('UNILAG LIBRARY','UNILAG',2000,"ELECTRICITY",1111221,"PHYSICS")

print(book1,journal1,mag,ref, sep="\n")
