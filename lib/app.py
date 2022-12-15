from lib.user import User
import csv
from lib.books import Book


def mandatory_input(text: str):
    value = ""
    while value == "":
        value = input(text)
    return value


class App:
    cuser = 'NO CUSER'

    def __init__(self):
        self.list_of_user = self.csv_to_list_user()

    @staticmethod
    def create_user() -> User:
        matricule = mandatory_input("Enter your id (ex : HEXXXXXX)\n")
        firstname = mandatory_input("Enter your firstname \n")
        lastname = mandatory_input("Enter your lastname \n")
        mail = mandatory_input("Enter your email address \n")
        address = mandatory_input("Enter your address \n")
        birth_date = mandatory_input("Enter your birth date (DD/MM/YYYY) \n")

        user = User(matricule, firstname, lastname, mail, address, birth_date)
        user.store_user()
        # user = User("201992", firstname, "Saragossi", "test@ephec.be", " address", "03/05/1996")
        return user

    @staticmethod
    def csv_to_list_user():
        with open('users.csv', newline='') as csvfile:
            list_of_user = []
            reader = csv.DictReader(csvfile)
            for row in reader:
                user = User(row['matricule'], row['prenom'], row['nom'], row['mail'], row['adresse'], row['Dnaissance'])
                list_of_user.append(user)
        return list_of_user

    def list_of_user_to_csv(self):
        with open("users.csv", "r+", newline='') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(['matricule', 'prenom', 'nom', 'mail', 'adresse', 'Dnaissance'])
            for user in self.list_of_user:
                writer.writerow([user.id_user, user.firstname, user.lastname, user.mail, user.address, user.birth_date])

    def verify_user(self):
        list_of_user = self.csv_to_list_user()
        app = App()
        matricule = mandatory_input("Entrez votre matricule : ")
        if matricule in [x.id_user for x in list_of_user]:
            App.cuser = matricule
            return app
        return False

    @classmethod
    def csv_to_list_of_books(cls):
        """
        Return a list of books
        """
        with open("library.csv", newline='') as csvfile:
            list_of_books = []
            reader = csv.DictReader(csvfile)
            for row in reader:
                book = Book(row['title'], row['status'], row['authors'], row['publisher'], row['person'])
                list_of_books.append(book)

        return list_of_books
