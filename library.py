#!python3
# -*- coding : utf-8 -*-

from books import Book
import csv  # To read csv and write on it


class Library:
    def __init__(self, file='library.csv'):
        self._library = self.csv_to_list_of_books(file)

    def __str__(self):
        lib_str = '{:^8}|{:^25}|{:^25}|{:^25}|{:<8}|{:^15}\n' \
                  '{}\n'.format('ID', 'Title', 'Authors', 'Publisher', 'Statut', 'Who', '-' * 110)
        for book in self.library:
            lib_str += str(book) + '\n'
        return lib_str

    @property
    def library(self):
        return self._library

    @staticmethod
    def csv_to_list_of_books(file):
        """
        Return a list of books
        :param file: The library that we want to read from
        :return: a list contenting all the books
        """
        with open(file, newline='') as csvfile:
            list_of_books = []
            reader = csv.DictReader(csvfile)
            for row in reader:
                book = Book(row['title'], file, row['status'], row['authors'], row['publisher'])
                list_of_books.append(book)

        return list_of_books

    def is_in_library(self, title):
        """
        PRE: The title must match the EXACT title in the library and the list of books must be in the format of a list
        of books coming from the function csv_to_list_of_books
        POST: /
        :param title: the EXACT title of the book we are looking for
        :return: True or False depending on if the library contain the book or not based on his title
        """
        # For points : using lambda and filter fonction : map
        title_list = list(
            map(lambda x: x.title, self.library))  # We create a list contenting all the title of the books
        if title in title_list:
            return True
        return False

    def take_a_book(self, title):
        """
        Remove a book from library
        :param title: a string that we will look for in the file library
        :return: print the title of the book if manage to book otherwise raise exception : No books found
        """
        # Check if the book is in the library otherwise
        if self.is_in_library(title):
            book = list(filter(lambda x: x.title == title, self.library))
            self.remove_book(title)
            print(f"{book[0]} successfully rented")
        else:
            # If the book is not in the library display some message
            print("\nThe book has not been found.\nLook for any typo in the title "
                  "and remember that the title is case sensitive.\n"
                  "If you don't know the name look for the --show argument "
                  "to see the list of book available at the moment")

    def remove_book(self, title):
        """
        function to remove rented book from library list
        PRE: The library file must exist and title must be present in library
        POST: The rented book is removed from library list
        """
        new_catalogue = list(filter(lambda x: x.title != title, self.library))
        print(new_catalogue)
        with open("library.csv", "w", newline='') as file:
            fieldnames = ['title', 'authors', 'publisher', 'status']
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            for item in new_catalogue:
                writer.writerow({'title': item.title, 'authors': item.authors,
                                 'publisher': item.publisher, 'status': item.status})
