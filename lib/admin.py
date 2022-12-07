#!python3
# -*- coding : utf-8 -*-

from lib.user import User
import hashlib

class Admin(User):
    def __init__(self,firstname,lastname):
        super().__init__(firstname,lastname)
        #self._firstname = firstname
        #self._lastname = lastname
        self._username = "admin"
        self._password = self.hash_password("admin")

    def change_password(self):
        if self.login():
            print("change ton mot de passe...")
            self._password = input("Entrez votre nouveau password : ")
            print(("Password changed succesfully"))
            self._password = self.hash_password(self._password)
    
    def hash_password(self, password):
        m = hashlib.sha256()
        m.update(password.encode("utf8"))
        return m.hexdigest()
    
    def login(self):
        username = input("Entrez votre nom d'utilisateur : ")
        password = input("Entrez votre password : ")
        password = self.hash_password(password)
        if username == self._username and password == self._password:
            print("loging in succesfully")
            return 1
        else:
            print("bad password")
            return 0
