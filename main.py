# This is a sample Python script.
import sys  # Access to argv and other stuff
import csv  # To read csv and write on it
import Books as b  # Import the class file of books who manage the creation and displaying of books
import argparse  # Used to create interaction directly from the commandline


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
    :param title: a string that we will look for in the file librairy
    :param library: The path to the file library
    :return: print the title of the book if manage to book otherwise raise exception : No books found
    """
    pass


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
    # ArgumentParser is an object that will contains all the arguments that we add to it with the command add_arguments
    parser = argparse.ArgumentParser(description="Display the list of all books contened in library",
                                     usage="Library management tool")
    # Adding the argument --library where we can specify wich file we can access
    parser.add_argument("-l", "--library", type=str, default="library.csv",
                        help="Show all the books title and author there is in the library")
    parser.add_argument("-s", "--search", type=str, default="",
                        help="Search and print if the library contains the book title that you pass in argument,"
                             " the title must be the exact same as the one stored in library")
    # Parsing all the args in one variable so we can access to it in the code with args.{variable_name}
    args = parser.parse_args()
    # Print all the args
    print("Args : {}".format(args))
    # Print all the books contained in the library
    print_books(args.library)
    # print(csv_to_list_of_book(args.library))
    # Print if the books is in the library if the arguments of search is going.
    if args.search:
        print(is_in_library(args.search, csv_to_list_of_books(args.library)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
