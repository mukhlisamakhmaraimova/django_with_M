from django.shortcuts import render

# Create your views here.


class Accounts:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        return f'My name is {self.name} \n I\'m {self.age}'

    def get_address(self):
        return f"My address: {self.address}"



