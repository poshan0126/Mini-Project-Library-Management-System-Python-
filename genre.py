from book import BookOperations
class Genre:
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category

    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def category(self):
        return self.__category

    # Setters
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @category.setter
    def category(self, new_category):
        self.__category = new_category

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"Description: {self.__description}\n"
                f"Category: {self.__category}")

class GenreOperations:
    def __init__(self):
        self.genres = []
        self.book_operations = BookOperations()

    def add_genre(self, genre):
        self.genres.append(genre)
        return f"Genre '{genre.name}' has been added."

    def view_genre_details(self, name):
        for genre in self.genres:
            if genre.name == name:
                return str(genre)
        return "Genre not found."

    def display_all_genres(self):
        return "\n".join(str(genre) for genre in self.genres)
    def display_books_by_genre(self, genre_name):
        books_by_genre = [book for book in self.book_operations.books if book.genre == genre_name]
        if books_by_genre:
            return "\n".join(str(book) for book in books_by_genre)
        else:
            return f"No books found in genre {genre_name}."
