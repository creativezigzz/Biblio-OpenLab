#!python3
# -*- coding : utf-8 -*-

class Address():
    def __init__(self, street, number, city):
        self._street = street
        self._number = number
        self._city = city

    def __str__(self):
        return f'{self.street} {self.number}, {self.city}\n'

    @property
    def city(self):
        return self._city

    @property
    def street(self):
        return self._street

    @property
    def number(self):
        return self._number

    def set_street(self, value):
        self._street = value

    def set_city(self, value):
        self._city = value

    def set_number(self, value):
        self._number = value
    # @street.setter
    # def street(self, new_street):
    #     self._street = new_street
    #
    # @number.setter
    # def number(self, new_number):
    #     self._number = new_number
    #
    # @city.setter
    # def city(self, new_city):
    #     self._city = new_city
