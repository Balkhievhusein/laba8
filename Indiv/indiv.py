#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

if __name__ == '__main__':
    school = {
        "1a": 20,
        "1b": 15,
        "2b": 33,
        "5a": 17,
        "7b": 15,
    }
    print(school)


    def add():

        className = input("Ввидите номер интересующего вас класса ")
        studentsCount = input("Будьте добры и пожалуйста ввидите количество учеников")
        school[className] = studentsCount
        print("Готова!")


    def change():
        add()


    def delete():
        cName = input("class name: ")
        del school[cName]


    while True:
        command = input("Внимателно читаю, что вы хотите? ")
        if (command == "add"):
            add()
        elif (command == "list"):
            print(school)
        elif (command == "change"):
            change()
        elif (command == "delete"):
            delete()