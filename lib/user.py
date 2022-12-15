import csv


class User:

    def __init__(self, id_user, firstname, lastname, mail, address, birth_date):
        self.__id_user = id_user
        self.__firstname = firstname
        self.__lastnmame = lastname
        self.__mail = mail
        self.__address = address
        self.__birth_date = birth_date

    @property
    def id_user(self):
        return self.__id_user

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastnmame

    @property
    def mail(self):
        return self.__mail

    @property
    def address(self):
        return self.__address

    @property
    def birth_date(self):
        return self.__birth_date

    def check_account(self):
        pass

    def __str__(self):
        return f"matricule {self.__id_user}, prenom {self.__firstname}, nom : {self.__lastnmame}, mail: {self.__mail}\
        , adresse : {self.__address}, date_naiss : {self.__birth_date} "

    def store_user(self):
        with open("users.csv", "a", newline='') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([self.id_user, self.firstname, self.lastname, self.mail, self.address, self.birth_date])
