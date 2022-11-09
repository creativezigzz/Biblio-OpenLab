#!python3
# -*- coding : utf-8 -*-

import os  # To use delete and rename
import csv  # To read csv and write on it
import Books as b  # Import the class file of books who manage the creation and displaying of books
import argparse  # Used to create interaction directly from the commandline


# def remove_book(title, catalogue):
#     """
#     function to remove rented book from library list
#     PRE: The library file must exist and title must be present in library
#     POST: The rented book is removed from library list
#     """
#     new_catalogue = list(filter(lambda x: x.title != title, catalogue))
#     with open ("library.csv", "w+") as file:
#         file.write("title, author")
#         for item in catalogue:
#             file.write(f"{item.title},{item.author}\n")

def print_books(library='library.csv'):
    """
    Function to print all the books from a csv file called(library.csv)
    PRE:the library file must exist.
    POST: Print all the books in the format : Title - Author
    RAISE: If no books in the library should raise an Exception : LibraryEmpty
    """
    with open(library, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book = b.Book(row['title'], row['author'])
            print(book)


def take_a_book(title, library):
    """
    :param title: a string that we will look for in the file library
    :param library: The path to the file library
    :return: print the title of the book if manage to book otherwise raise exception : No books found
    """
    # Check if the book is in the library otherwise
    if is_in_library(title, csv_to_list_of_books(library)):
        with open(library, 'r', newline='') as f_reader:
            with open("temp.csv", 'w', newline='') as f_writer:
                # reader for the file
                f1 = csv.reader(f_reader)
                # writer of the file
                f2 = csv.writer(f_writer)  # creating a temp file for writing
                for row in f1:  # Look over the whole file
                    if title not in row[0]:  # if the title is not in the row he will write the book
                        f2.writerow(row)  # write the row in the file
                    else:
                        book_rented = b.Book(row[0], row[1])  # The book that we rent
                        print("{} has been successfully rented \n Thank you for using our library system".format(
                            book_rented))  # Print in the console the book that we rent
        os.rename(library, "dump.csv")
        os.rename("temp.csv", library)
        os.remove("dump.csv")
    else:
        # If the book is not in the library display some message
        print("\nThe book has not been found.\nLook for any typo in the title "
              "and remember that the title is case sensitive.\n"
              "If you don't know the name look for the --show argument "
              "to see the list of book available at the moment")


def is_in_library(title, list_of_books):
    """
    PRE: The title must match the EXACT title in the library and the list of books must be in the format of a list
    of books coming from the function csv_to_list_of_books
    POST: /
    :param title: the EXACT title of the book we are looking for
    :param list_of_books: A list contenting all the book object.
    :return: True or False depending on if the library contain the book or not based on his title
    """
    # For points : using lambda and filter fonction : map
    title_list = list(map(lambda x: x.title, list_of_books))  # We create a list contenting all the title of the books

    if title in title_list:
        return True
    return False


def csv_to_list_of_books(csv_file):
    """
    :param csv_file: The library that we want to read from
    :return: a list contening all the books
    """
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_book = []
        for row in reader:
            book = b.Book(row['title'], row['author'])
            list_book.append(book)

    return list_book


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create the argparse to content all the arguments pass to the terminal
    # ArgumentParser is an object that will contain all the arguments that we add to it with the command add_arguments
    parser = argparse.ArgumentParser(description="Display the list of all books contened in library",
                                     usage="Library management tool")
    # Adding the argument --library where we can specify wich file we can access default is "library.csv"
    parser.add_argument("-l", "--library", type=str, default="library.csv",
                        help="Choose the file contenting the library. Default is library.csv")
    # Adding the argument --search to know if the book is in the library or not
    parser.add_argument("-s", "--search", type=str, default="",
                        help="Search and print if the library contains the book title that you pass in argument,"
                             " the title must be the exact same as the one stored in library")
    # Adding the argument --rent to rent a book and display the title + author  of the book rented
    parser.add_argument("-r", "--rent", type=str, help="Rent a book, remove it from the libray and will display the "
                                                       "title + author of the book that you just rent")
    # Adding the argument --show to show all the books present in the library
    parser.add_argument("-sh", "--show", type=bool, default=False,
                        help="Show all the books present in the library, it's a boolean so True or False")
    # Parsing all the args in one variable, so we can access to it in the code with args.{variable_name}
    args = parser.parse_args()
    # Print all the args
    # print("Args : {}".format(args))
    # Print all the books contained in the library if the --library argument is present
    # print_books(args.library)
    # print(csv_to_list_of_book(args.library))
    # Print if the books is in the library if the arguments of search is going.
    if args.show:
        print_books(args.library)
    if args.search:
        print(is_in_library(args.search, csv_to_list_of_books(args.library)))
    if args.rent:
        take_a_book(args.rent, args.library)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
