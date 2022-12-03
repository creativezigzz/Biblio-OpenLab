#!python3
# -*- coding : utf-8 -*-

import argparse  # Used to create interaction directly from the commandline
from lib.library import Library

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create the argparse to content all the arguments pass to the terminal
    # ArgumentParser is an object that will contain all the arguments that we add to it with the command add_arguments
    parser = argparse.ArgumentParser(description="Library management tool to let students rent educational books",
                                     usage="Biblio 2.0")
    # Adding the argument --library where we can specify which file we can access default is "library.csv"
    parser.add_argument("-l", "--library", type=str, default="library.csv",
                        help="Choose the file contenting the library. Default is library.csv")
    # Adding the argument --search to know if the book is in the library or not
    parser.add_argument("-s", "--search", type=str, default="",
                        help="Search and print if the library contains the book title that you pass in argument,"
                             " the title must be the exact same as the one stored in library")
    # Adding the argument --rent to rent a book and display the title + author  of the book rented
    parser.add_argument("-r", "--rent", type=str, help="Rent a book, remove it from the libray and will display the "
                                                       "title + author of the book that you just rent.\n "
                                                       "The search are case sensitive so the title must be "
                                                       "the exact same as the one stored in library")
    # Adding the argument --show to show all the books present in the library
    parser.add_argument("-sh", "--show", default=False, action='store_true',
                        help="Show all the books present in the library")
    # Parsing all the args in one variable, so we can access to it in the code with args.{variable_name}
    args = parser.parse_args()
    # Print all the args
    # print("Args : {}".format(args))
    library = Library(args.library)
    # Show all the library
    if args.show:
        print(library)
        # Print if the books is in the library if the arguments of search is going.
    if args.search:
        print(library.is_in_library(args.search))
    if args.rent:
        library.take_a_book(args.rent)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
