from book import BookOperations
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def biography(self):
        return self.__biography

    # Setters
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @biography.setter
    def biography(self, new_biography):
        self.__biography = new_biography

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"Biography: {self.__biography}")

class AuthorOperations:
    def __init__(self):
        self.book_operations = BookOperations()
        self.authors = []

    def add_author(self, author):
        self.authors.append(author)
        return f"Author '{author.name}' has been added."

    def view_author_details(self, name):
        for author in self.authors:
            if author.name == name:
                return str(author)
        return "Author not found."

    def display_all_authors(self):
        return "\n".join(str(author) for author in self.authors)
    def display_books_by_author(self, author_name):
        books_by_author = [book for book in self.book_operations.books if book.author == author_name]
        if books_by_author:
            return "\n".join(str(book) for book in books_by_author)
        else:
            return f"No books found by author {author_name}."
