# This is a sample Python script.
import csv
import Books as b


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_books(library='library.csv'):
    """
    Function to print all the books from a csv file called(library.csv)
    PRE:the library file must exist.
    POST: Print all the books in the format : Title - Author
    RAISE: If no books in the librairy should raise an Exception : LibrairyEmpty
    """
    with open(library,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book = b.Book(row['title'],row['author'])
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
    print_hi('PyCharm')
    b1 = b.Book("Coucou", "Unknow")
    print_books()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
