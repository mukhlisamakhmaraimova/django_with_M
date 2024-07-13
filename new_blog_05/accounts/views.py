from django.shortcuts import render

# Create your views here.


class Accounts:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'My name is {self.name} \n I\'m {self.age}'

