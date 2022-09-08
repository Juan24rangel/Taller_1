# Hallar el mayor de tres numeros

print("----------------------------")
print("-----MAYOR DE 3 ENTEROS-----")
print("----------------------------")

# input
a = int(input("digite el valor del primer numero: "))
b = int(input("digite el valor del segundo numero: "))  
c = int(input("digite el valor del tercer numero: "))

#processing
if a>b:
    if a>c:
        mayor = a
    else:
        mayor = c
else:
    if b>c:
        mayor = b
    else:
        mayor = c
        
#output
print("----------------------------")
print("---------RESULTADO----------")
print("----------------------------")
print("el mayor entre " +str(a) + " , " +str(b) + " y " +str (c) + " es: " +str(mayor))
