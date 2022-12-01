#!python3
# -*- coding : utf-8 -*-
import csv
import os
from books import Book


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

    def __init__(self, local):
        self._local = local
        self._sections = []

    def add_sections(self):
        # Add all the section in a list we can iterate
        list_sections = listdirs(f'./Locations/{self.local}')
        for section_path in list_sections:
            section = Section(section_path)
            self.sections.append(section)

    @property
    def local(self):
        return self._local

    @property
    def sections(self):
        return self._sections


class Section(Location):
    def __init__(self, section_path):
        super().__init__(self)
        self._section_path = section_path
        self._bookshelves = []

    @property
    def section_path(self):
        return self._section_path

    @property
    def bookshelves(self):
        return self._bookshelves

    def add_bookshelves(self):
        list_bookshelves = listfile(self.section_path)
        for bookshelf_path in list_bookshelves:
            bookshelf = BookShelf(bookshelf_path)
            self._bookshelves.append(bookshelf)


class BookShelf(Section):
    def __init__(self, bookshelf_path):
        super().__init__(self)
        self._bookshelf_path = bookshelf_path
        self._books = self.csv_to_list_of_books(bookshelf_path)

    def __str__(self):
        lib_str = '\nBookshelves : {:<23}| Section : {:<23}\n' \
                  '{:^8}|{:^25}|{:^25}|{:^25}|{:<8}|{:^15}\n{}\n' \
            .format(os.path.basename(self.bookshelf_path), "Section",
                    'ID', 'Title', 'Authors', 'Publisher', 'Status',
                    'Who', '-' * 110)
        for book in self.books:
            lib_str += str(book) + '\n'
        return lib_str + '\n \n '

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


l = Location('L101')
l.add_sections()
for s in l.sections:
    s.add_bookshelves()
    for b in s.bookshelves:
        print(b)
