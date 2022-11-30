#!python3
# -*- coding : utf-8 -*-

import itertools


class Book:
    id_book = itertools.count()

    def __init__(self, title, library, status, author='Unknown', publisher='Unknown', person='Michel'):
        """This creates a new instance of Book with a title and author"""
        self._title = title
        self._author = author
        self._id = next(Book.id_book)
        self._publisher = publisher
        self._status = status
        self.library = library
        self._person = person

    def __str__(self):
        b = "{:^8}| {:<23.23} | {:<23.23} | {:<23.23} | {:<8} | {:^15}" \
            .format(self.id, self.title, self.author, self.publisher,
                    'Loué' if not self.status == 'true' else 'Libre',
                    '/' if self.status == 'true' else self.person)
        return b

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def id(self):
        return self._id

    @property
    def publisher(self):
        return self._publisher

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, new_person):
        self._person = new_person

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, s):
        if s == 'true':
            self._status = s
        else:
            self.person = '/'
            self._status = s

    def __del__(self):
        pass
