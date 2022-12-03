#!python3
# -*- coding : utf-8 -*-

from user import User

class Admin(User):
    def __init__(self,firstname,lastname):
        super().__init__(firstname,lastname)
        #Trouvez ce qui le différencie des autres users maybe un password ?
        pass

