# Cuanto dura y cuesta una llamada

print("----------------------------")
print("---------TIEMPO-COSTO-------")
print("----------------------------")

#input

t=input("digite el valor del tiempo: ")
t=int (t)
#processing
if t<=3:
     costo = 300
else:
    if t >= 3:
        costo = 300 + (t*50)
    
#output
print("----------------------------")
print("---------RESULTADO----------")
print("----------------------------")
print("el precio es: " +str(costo)+"$")

#fin