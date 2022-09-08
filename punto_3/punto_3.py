# Comprobar que un numero de 4 cifras es positivo

 



import netrc
import numbers
import pathlib
from tkinter import N


print("----------------------------")
print("-------------VALOR----------")
print("----------------------------")

#input

x = input("Digite valor del numero: ")
x = int(x)

#processing
if x<999:
    valor = ("no cumple")
else:
    if x>999:
        valor = ("cumple")
#output
print("----------------------------")
print("---------RESULTADO----------")
print("----------------------------")
print("¿cumple la condicion?: " +str(valor))

#fin