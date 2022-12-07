#!python3
# -*- coding : utf-8 -*-

import argparse  # Used to create interaction directly from the commandline
from lib.library import Library
from lib.admin import Admin as admin
import sys

def back_to_main_menu():
    choice = ''
    while choice != 'b':
        choice = input("Type 'b' to go back to main menu : ")
                    
    display_main_menu()

def display_main_menu():
            print("-----   MENU   -----\n")
            print("1. Montrer la charte d'utilisation")
            print("2. Rendre un livre")
            print("3. Louer un livre")
            print("4. Espace admin")
            print("5. faire une recherche dans le catalogue de la bibliothèque")
            print("6. Créer un profil")
            print("7. Montrer le catalogue")
            print("8. Quitter")

            menu_choice = input("Entrez le numéro de votre choix : ")
            
            if menu_choice == "1":
                print("Voici la charte d'utilisation")
                choice = ''
                back_to_main_menu()
            elif menu_choice == "2":
                library.return_a_book()
                back_to_main_menu()
            elif menu_choice == "3":
                library.take_a_book()
                back_to_main_menu()
            elif menu_choice == "4":
                if admin.login():
                    display_admin_menu()
                back_to_main_menu()
            elif menu_choice == "5":
                title_search = input("Tapez votre recherche : ")
                library.is_in_library(title_search)
                back_to_main_menu()
            elif menu_choice == "6":
                print("Créez votre profil")
                back_to_main_menu()
            elif menu_choice == "7":
                print(library)
                back_to_main_menu()
            elif menu_choice == "8":
                library.list_of_books_to_csv()
                sys.exit()
            else:
                print("\n[!] Le choix que vous avez fait n'existe pas!\n")
                display_main_menu()

def display_admin_menu():
        print("-----   MENU admin   -----\n")
        print("1. Modifier le mot de pass administrateur")
        print("2. Statistiques")
        print("3. Gestion des Avertissements")

        menu_choice = input("Entrez le numéro de votre choix ou 'b' pour retourner au menu principal: ")
        
        if menu_choice == "1":
            admin.change_password
            pass
        elif menu_choice == "2":
            print("Menu statistiques\n\tEn construction\n")
            display_admin_menu()
        elif menu_choice == "3":
            print("Gestion des avertissements\n\tEn construction\n")
            display_admin_menu()
        elif menu_choice == 'b':
            display_main_menu()

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
    parser.add_argument("-m", "--menu", type=bool, default=False, help="Voyager à l'aide du menu")
    # Parsing all the args in one variable, so we can access to it in the code with args.{variable_name}
    args = parser.parse_args()
    # Print all the args
    # print("Args : {}".format(args))
    library = Library(args.library)
    admin = admin('jean-Patrick', 'Benjamin')
    # Show all the library
    if args.show:
        print(library)
        # Print if the books is in the library if the arguments of search is going.
    if args.search:
        print(library.is_in_library(args.search))
    if args.rent:
        library.take_a_book(args.rent)
    if args.menu:
        display_main_menu()
