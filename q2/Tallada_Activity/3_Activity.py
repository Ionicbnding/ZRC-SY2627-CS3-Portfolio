
class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # Getter for title
    def get_title(self):
        return self.__title

    # Getter for author
    def get_author(self):
        return self.__author

    # Setter for title
    def set_title(self, title):
        self.__title = title

    # Setter for author
    def set_author(self, author):
        self.__author = author

    # Display publication information
    def display_info(self):
        print("Title:", self.get_title())
        print("Author:", self.get_author())


class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = 1
        self.set_number_of_pages(number_pages)

    # Getter for number of pages
    def get_number_of_pages(self):
        return self.__number_of_pages

    # Setter for number of pages
    def set_number_of_pages(self, number_pages):
        if isinstance(number_pages, int) and not isinstance(number_pages, bool) and number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print("The number of pages must be positive.")

    # Display book information
    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.get_number_of_pages())


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 1
        self.set_issue_number(issue_number)

    # Getter for issue number
    def get_issue_number(self):
        return self.__issue_number

    # Setter for issue number
    def set_issue_number(self, issue_number):
        if isinstance(issue_number, int) and not isinstance(issue_number, bool) and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    # Display magazine information
    def display_info(self):
        super().display_info()
        print("Issue Number:", self.get_issue_number())


# Create two Publication objects
publication1 = Publication("Library Science", "John Smith")
publication2 = Publication("Education Today", "Mary Jones")

# Create two Book objects
book1 = Book("Harry Potter", "J.K. Rowling", 350)
book2 = Book("The Little Prince", "Antoine de Saint-Exupery", 96)

# Create two Magazine objects
magazine1 = Magazine("National Geographic", "Susan Goldberg", 12)
magazine2 = Magazine("Time Magazine", "Sam Jacobs", 25)


# Display all objects
print("===== PUBLICATIONS =====")
publication1.display_info()
print()
publication2.display_info()

print("\n===== BOOKS =====")
book1.display_info()
print()
book2.display_info()

print("\n===== MAGAZINES =====")
magazine1.display_info()
print()
magazine2.display_info()
