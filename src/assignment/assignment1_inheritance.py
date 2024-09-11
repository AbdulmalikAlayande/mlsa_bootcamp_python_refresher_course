def skip_lines():
    for _ in range(3):
        print()


class LibraryItem:

    def __init__(self, title: str, author: str, publication_year: str):
        super().__init__()
        self._title: str = title
        self._author: str = author
        self._publication_year: str = publication_year
        print(self)

    def __str__(self) -> str:
        return """
                Title: {0}
                Author: {1}
                Publication Year: {2}
               """.format(
            self._title, self._author, self._publication_year
        )

    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self._author

    def get_publication_year(self) -> str:
        return self._publication_year

    def set_title(self, title: str) -> None:
        self._title = title

    def set_author(self, author: str) -> None:
        self._author = author

    def set_publication_year(self, publication_year: str) -> None:
        self._publication_year = publication_year

    def borrow(self) -> None:
        print("Book borrowed from the Library")


class Book(LibraryItem):

    def __init__(self, genre: str, isbn: str) -> None:
        self._genre: str = genre
        self._isbn: str = isbn

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"""
                Genre: {self._genre}
                ISBN: {self._isbn}
                """
        )


class Journal(LibraryItem):

    def __init__(self, volume: int, issue: int):
        self._volume = volume
        self._issue = issue

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"""
                Volume: {self._volume}
                Issue: {self._issue}
                """
        )


class Magazine(LibraryItem):
    def __init__(self, issue_month: str, editor: str):
        self._issue_month: str = issue_month
        self._editor: str = editor

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"""
                Issue Month: {self._issue_month}
                Editor: {self._editor}
                """
        )


class ReferenceBook(LibraryItem):
    def __init__(self, reference_section: str):
        self._reference_section = reference_section

    def borrow(self) -> None:
        print(
            "We are so sorry, The Issuance of Reference books are restricted to certain customers."
        )

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"""
                Reference Section: {self._reference_section}
                """
        )


book1 = Book("Fiction", "1234567890")
book1.set_title("Things Fall Apart")
book1.set_author("Chinua Achebe")
book1.set_publication_year("1976")
print(book1)
book1.borrow()

skip_lines()

journal1 = Journal(1, 2)
journal1.set_title("Nigeria Is A Joke")
journal1.set_author("Dele Momodu")
journal1.set_publication_year("1988")
print(journal1)
journal1.borrow()

skip_lines()

magazine1 = Magazine("January", "John Doe")
magazine1.set_title("Most Irrational Celebrities")
magazine1.set_author("Very Dark Man")
magazine1.set_publication_year("2024")
print(magazine1)
magazine1.borrow()
skip_lines()

reference_book1 = ReferenceBook("Science")
reference_book1.set_title("Just A Reference")
reference_book1.set_author("I said it's just a reference")
reference_book1.set_publication_year("you don't seem to have listening ears")
print(reference_book1)
reference_book1.borrow()
