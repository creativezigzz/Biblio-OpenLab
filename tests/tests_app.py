from lib.app import App
from unittest import TestCase

class AppTestCase(TestCase):
    # vérifier que la variable d'instance est établit / self.csv_to_list_user(file)
    def test_init(self):
        self.assertEqual(list(map(lambda user: user.id_user, App("../tests/tests_users.csv").list_of_user)), ["he201992", "he212121"])

    def test_csv_to_list_users(self):
        # user = paramètre de la lamda
        # user.matricule = valeur de retour
        # il va chercher le fichier dans lib et pas à la racine
        self.assertEqual(list(map(lambda user: user.id_user, App.csv_to_list_user("../tests/tests_users.csv"))), ["he201992", "he212121"])
        # donner un fichier qui n'existe pas à list_of_user_to_csv

        # 1: App() --> charger le contenu de users.csv dans la variable d'instance list_of_users
        # 2: appelle la fonction list_of_user_to_csv() et on enregistre le contenu de la variable d'instance
        # list_of_user dans le fichier ../tests/tests_users.csv"
        # 3 : Vérifier que le contenu de test_user.csv est = au contenu de users.csv
    def test_list_of_user_to_csv(self):
        App("../tests/tests_users.csv").list_of_user_to_csv("../tests/list_of_user_to_csv.csv") #copie le contenu de tests_users.csv vers list_of_user_to_csv.csv
        self.assertEqual(list(map(lambda user: user.id_user, App.csv_to_list_user("../tests/list_of_user_to_csv.csv"))), ["he201992", "he212121"]) # on vérifie que list_of user contiennent bien les matricules connus

    def test_csv_to_list_of_books(self):
        self.assertEqual(list(map(lambda book: book.title, App.csv_to_list_of_books("../tests/tests_csv_to_list_of_books.csv"))), ["Ready for more time", "From time to time app"])

    def test_csv_to_list_user_with_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            App.csv_to_list_user("test")

    def test_csv_to_list_of_books_with_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            App.csv_to_list_of_books("test")

    def test_list_of_user_to_csv_with_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            App.csv_to_list_of_books("test")