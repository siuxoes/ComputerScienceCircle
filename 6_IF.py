__author__ = 'Siuxoes'
# -*- coding: utf-8 -*-

from datetime import date

anioActual = date.today().year

anioNacimiento = int(input("Introduce tu año de nacimiento: "))

edad = anioActual - anioNacimiento

print("Tienes", edad, "años")