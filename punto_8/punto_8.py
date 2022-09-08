# Hallar raices de una ecuacion cuadratica

from cmath import sqrt


print("----------------------------")
print("-------------VALOR----------")
print("----------------------------")
#input
a = float(input("Digite valor del numero a: "))
b = float(input("Digite valor del numero b: "))
c = float(input("Digite valor del numero c: "))
#processing

discriminante = b*b - 4*a*c

if discriminante < 0:
    ("la ecuacion no tiene solución") 

raiz = sqrt(discriminante)
x1 = (-b + raiz) / (2*a)
x2 = (-b - raiz) / (2*a)
#output

print ("el valor de x1 es: "+str(x1) + "el  valor de x2 es:" +str(x2))
