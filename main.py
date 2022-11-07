# This is a sample Python script.
import sys  # Access to argv and other stuff
import csv  # To read csv and write on it
import Books as b  # Import the class file of books who manage the creation and displaying of books
import argparse


def print_books(library='library.csv'):
    """
    Function to print all the books from a csv file called(library.csv)
    PRE:the library file must exist.
    POST: Print all the books in the format : Title - Author
    RAISE: If no books in the librairy should raise an Exception : LibrairyEmpty
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create the argparse to content all the arguments pass to the terminal
    # ArgumentParser is an object that will contains all the arguments that we add to it with the command add_arguments
    parser = argparse.ArgumentParser(description="Display the list of all books contened in library")
    # Adding the argument --library where we can specify wich file we can access
    parser.add_argument("-l", "--library", type=str, default="library.csv",
                        help="Show all the books title and author there is in the library")
    # Parsing all the args in one variable so we can access to it in the code with args.{variable_name}
    args = parser.parse_args()
    # Print all the args
    print("Project title {}".format(args))
    # Print all the books contained in the library
    print_books(args.library)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
