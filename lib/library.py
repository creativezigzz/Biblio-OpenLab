#!python3
# -*- coding : utf-8 -*-

from lib.books import Book
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
        PRE: Library have to exist
        POST: /
        :param title: string that we want to search among titles of the ibrary
        :return:
        """
        # For points : using lambda and filter fonction : map
        title_list = [print(str(x)) for x in self.library if title in x.title]
        if len(title_list) == 0:
            print(f"No match found in the library with : {title}")
            return False
        else:
            return True
            #map(lambda x: x.title, self.library))  # We create a list contenting all the title of the books
        # if title in title_list:
        #     return True
        # return False

    def take_a_book(self):
        """
        Remove a book from library
        :param title: a string that we will look for in the file library
        :return: print the title of the book if manage to book otherwise raise exception : No books found
        """
        # Check if the book is in the library otherwise
        book_rent = input("Quel livre voulez-vous louer? : ")
        if self.is_in_library(book_rent):
            my_choice = int(input("Which ID do you want to rent? : "))
            for book in self.library:
                if my_choice == book.id:
                    if book.status == 'Libre':
                        book.status = 'Loué'
                        print(f"The book '{book.title}' successfully rented")
                    else:
                        print("Le livre que vous voulez louer n'est pas libre")
        else:
            # If the book is not in the library display some message
            print("\nThe book has not been found.\nLook for any typo in the title "
                  "and remember that the title is case sensitive.\n"
                  "If you don't know the name look for the --show argument "
                  "to see the list of book available at the moment")

    def return_a_book(self):
        id_to_return = int(input("Quelle est l'ID du livre que vous voulez rendre ? : "))
        book_to_return = [x for x in self.library if x.id == id_to_return]
        for book in self.library:
            if id_to_return == book.id and book.status == "Loué":
                book.status = "Libre"
                book.person = '/'
                print(f"\n\t==> the book '{book.title} was succefuly returned\n")

    def list_of_books_to_csv(self):
        with open("library.csv", "r+",newline='') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(['title','authors','publisher','status'])
            for book in self.library:
                writer.writerow([book.title,book.authors,book.publisher,book.status])
    
    # def remove_book(self, title):
    #     """
    #     function to remove rented book from library list
    #     PRE: The library file must exist and title must be present in library
    #     POST: The rented book is removed from library list
    #     """
    #     new_catalogue = list(filter(lambda x: x.title != title, self.library))
    #     print(new_catalogue)
    #     with open("../library.csv", "w", newline='') as file:
    #         fieldnames = ['title', 'authors', 'publisher', 'status']
    #         writer = csv.DictWriter(file, fieldnames)
    #         writer.writeheader()
    #         for item in new_catalogue:
    #             writer.writerow({'title': item.title, 'authors': item.authors,
    #                              'publisher': item.publisher, 'status': item.status})
