class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availability=True):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = availability

    # Getters
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def genre(self):
        return self.__genre

    @property
    def publication_date(self):
        return self.__publication_date

    @property
    def availability(self):
        return self.__availability

    # Setters
    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @author.setter
    def author(self, new_author):
        self.__author = new_author

    @isbn.setter
    def isbn(self, new_isbn):
        self.__isbn = new_isbn

    @genre.setter
    def genre(self, new_genre):
        self.__genre = new_genre

    @publication_date.setter
    def publication_date(self, new_publication_date):
        self.__publication_date = new_publication_date

    @availability.setter
    def availability(self, new_availability):
        self.__availability = new_availability
    def __str__(self):
        return (f"Title: {self.__title}\n"
                f"Author: {self.__author}\n"
                f"ISBN: {self.__isbn}\n"
                f"Genre: {self.__genre}\n"
                f"Publication Date: {self.__publication_date}\n"
                f"Availability: {'Available' if self.__availability else 'Unavailable'}")

class BookOperations:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)

        print( f"Book '{book.title}' has been added to the library.")


    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.availability:
                    book.availability = False
                    return f"You have borrowed '{book.title}'."
                else:
                    return f"The book '{book.title}' is currently unavailable."
        return "Book not found."

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.availability:
                    book.availability = True
                    return f"You have returned '{book.title}'."
                else:
                    return f"The book '{book.title}' was not borrowed."
        return "Book not found."

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return str(book)
        return "Book not found."

    def display_all_books(self):
        return "\n".join(str(book) for book in self.books)
    def bookCLI():
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Quit")

            choice = input("\nChoose an operation: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                genre = input("Enter book genre: ")
                publication_date = input("Enter book publication date: ")
                book = Book(title, author, isbn, genre, publication_date)
                print(add_book(book))

            elif choice == '2':
                title = input("Enter book title: ")
                print(borrow_book(title))

            elif choice == '3':
                title = input("Enter book title: ")
                print(return_book(title))

            elif choice == '4':
                title = input("Enter book title: ")
                print(search_book(title))

            elif choice == '5':
                print(display_all_books())

            elif choice == '6':
                break

            else:
                print("Invalid choice. Please choose a valid operation.")
