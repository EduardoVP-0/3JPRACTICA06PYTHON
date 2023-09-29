#PRACTICA 06
#EDUARDO VELAZQUEZ

#Declara una lista de cadenas
aves=["Loro gris","Paloma de diamante","Coctel"]
print("Los valores de la lista antes de insertar son: ")

#Itera sobre la lista para imprimir valores

for ave in aves:
    print(ave, end=" ")
    
print("\n")

#Agrega tres valores al final de la lista utilizando el metodo append()
aves.append("Mayna")
aves.append("Periquitos")
aves.append("Cacatua")
print("Los valores de la lista despues de insertar:")
#Itera sobre la lista para imprimir los valores
for ave in aves:
    print(ave, end= " ")

print("\n")
