class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def library_id(self):
        return self.__library_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    # Setters
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @library_id.setter
    def library_id(self, new_library_id):
        self.__library_id = new_library_id

    # User-related functions
    def borrow_book(self, book):
        self.__borrowed_books.append(book)
        return f"User '{self.__name}' has borrowed the book '{book.title}'."

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            return f"User '{self.__name}' has returned the book '{book.title}'."
        else:
            return f"User '{self.__name}' did not borrow the book '{book.title}'."

    def __str__(self):
        borrowed_book_titles = "\n".join(str(book) for book in self.__borrowed_books)
        return (f"Name: {self.__name}\n"
                f"Library ID: {self.__library_id}\n"
                f"Borrowed Books: {borrowed_book_titles}")

class UserOperations:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        return f"User '{user.name}' has been added."
    def get_user_by_id(self, library_id):
        for user in self.users:
            if user.library_id == library_id:
                return user
        print("No user found with the given library ID.")
        return None

    def view_user_details(self, library_id):
        for user in self.users:
            if user.library_id == library_id:
                return str(user)
        return "User not found."

    def display_all_users(self):
        return "\n".join(str(user) for user in self.users)
