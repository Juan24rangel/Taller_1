# determinar si los dos ultimos digitos son iguales


print("----------------------------")
print("-------------VALOR----------")
print("----------------------------")

#input

x = int(input("Digite valor del numero: "))

# processing
d1 = x % 10
d2 = ((x%100)-d1)//10

if d1==d2:
    v = ("Si son iguales")
else:
    v = ("no son iguales")
    

#output
print("----------------------------")
print("---------RESULTADO----------")
print("----------------------------")
print("¿cumple la condicion?: " +str(v))