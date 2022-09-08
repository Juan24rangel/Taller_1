# Comprobar si el ultimo digito de un numero es par



print("----------------------------")
print("-------------VALOR----------")
print("----------------------------")

#input

numero = int(input("Digite valor del numero: "))

#processing

if numero %2 == 0:
    c = ("el ultimo es par")
else:
    c = ("el ultimo no es par")
            

#output

print("----------------------------")
print("---------RESULTADO----------")
print("----------------------------")
print("¿cumple la condicion?: " +str(c))


#fin