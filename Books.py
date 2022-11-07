class Book:

    def __init__(self, title, author):
        """This create a new instance of Book with a title and author"""
        self._title = title
        self._author = author

    def __str__(self):
        return " {} from {}".format(self.title, self.author)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
