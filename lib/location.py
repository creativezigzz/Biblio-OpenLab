#!python3
# -*- coding : utf-8 -*-
import csv
import os
from books import Book
from address import Address


def listfile(rootdir):
    list_file = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isfile(d):
            # print(d)
            list_file.append(d)
    return list_file


def listdirs(rootdir):
    list_dir = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            # print(d)
            list_dir.append(d)
            listdirs(d)
    return list_dir


class Location:
    """
    A location in the school where some books are situated
    """

    def __init__(self, local):
        self._local = local
        self._sections = []
        self._address = Address('-', '-', '-')

    def set_where(self):
        """
        Setting up the address of the location
        :return:
        """
        print("Set the address of the location")
        new_street = input("Street name: \n")
        new_number = input('Number of the house/building \n')
        new_city = input('City : \n')
        self.address.set_city(new_city)
        self.address.set_street(new_street)
        self.address.set_number(new_number)

    def add_sections(self):
        """
        Create and add all the sections from the root folder self_local in the variable self._sections
        pre: self.local must be an existing folder in the data system otherwise its created
        post: self_sections -> add all the sections_path folder from the root folder of the self._local
        raise: if the folder doesn't exist or path is incorrect raise an LocationException
        :return: a list of Section() that are contained in the self_local
        """
        # Add all the section in a list we can iterate
        # Path to the file Here we need to change some stuff to point to correct folder
        list_sections = listdirs(f'../Locations/{self.local}')
        for section_path in list_sections:
            section = Section(self.local, section_path,self.address)
            self.sections.append(section)

    @property
    def local(self):
        return self._local

    @property
    def sections(self):
        return self._sections

    @property
    def address(self):
        return self._address


class Section(Location):
    def __init__(self, local, section_path, address):
        """Initialize a new Section with the name of the local in it to access from it
         pre: self._section_path must be a correct path : "Locations/{super().local}/{self.section_path}"
         post: /
         """
        super().__init__(local)
        self._section_path = section_path
        self._section_number = os.path.basename(self.section_path)
        self._bookshelves = []
        self._address = address

    @property
    def address(self):
        return self._address

    @property
    def section_path(self):
        return self._section_path

    @property
    def bookshelves(self):
        return self._bookshelves

    @property
    def section_number(self):
        return self._section_number

    def add_bookshelves(self):
        """
               Create and add all the bookshelves from the section folder self_section_path in the variable self._bookshelves
               pre: self must be initialize from a location as it inherit from is parent
                    self can be empty

               post: self_bookshelves -> add all the bookshelves objects from the section folder of the self._section_path
               raise: if the folder doesn't exist or path is incorrect raise an LocationSectionException
               :return: a list of Bookshelf() that are contained in the self_bookshelves
               """
        # Add all the section in a list we can iterate
        list_bookshelves = listfile(self.section_path)
        for bookshelf_path in list_bookshelves:
            bookshelf = BookShelf(local=self.local, section_path=self.section_path, bookshelf_path=bookshelf_path,
                                  address=self.address)
            self._bookshelves.append(bookshelf)


class BookShelf(Section):
    def __init__(self, local, section_path, bookshelf_path, address):
        super().__init__(local, section_path, address)
        self._bookshelf_path = bookshelf_path
        self._books = self.csv_to_list_of_books(bookshelf_path)

    def __str__(self):
        """Print the bookshelf in the good format
        pre:if self is empty don't return Empty
        post:/
        raise: if self.bookshelf_path is in incorrect format ('folder/dir/file.csv') raise an LocationSectionBookshelfException
        :return: A string contenting all the books that are in the bookshelf.
        """
        lib_str = '\nBookshelf : {:<15} || \tSection : {:^15} || \tLocal : {:^15}\n' \
                  '{:^8}|{:^25}|{:^25}|{:^25}|{:<8}|{:^15}\n{}\n' \
            .format(os.path.basename(self.bookshelf_path), self.section_number, self.local,
                    'ID', 'Title', 'Authors', 'Publisher', 'Status',
                    'Who', '-' * 110)
        for book in self.books:
            lib_str += str(book) + '\n'
        return lib_str + '\n '

    @property
    def books(self):
        return self._books

    @property
    def bookshelf_path(self):
        return self._bookshelf_path

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

    def is_in_bookshelf(self, title):
        """
        PRE: The title must match the EXACT title in the library and the list of books must be in the format of a list
        of books coming from the function csv_to_list_of_books
        POST: /
        :param title: the EXACT title of the book we are looking for
        :return: True or False depending on if the library contain the book or not based on his title
        """
        # For points : using lambda and filter fonction : map
        title_list = list(
            map(lambda x: x.title, self.books))  # We create a list contenting all the title of the books
        if title in title_list:
            return True
        return False


# Uncomment to test location.py
# l = Location('L101')
# l.set_where()
# l.add_sections()
# for s in l.sections:
#     s.add_bookshelves()
#     for b in s.bookshelves:
#         print(b)
#         print(b.address)
