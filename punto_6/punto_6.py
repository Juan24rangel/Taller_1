# Si al sumar sus ultimos dos digitos da 1

print("----------------------------")
print("-------------VALOR----------")
print("----------------------------")

#input

x = int(input("Digite valor del numero: "))

# processing
d1 = x % 10
d2 = ((x%100)-d1)//10

if d1+d2==1:
    v = ("Si")
else:
    v = ("No")
    

#output
print("----------------------------")
print("---------RESULTADO----------")
print("----------------------------")
print("¿cumple la condicion?: " +str(v))
