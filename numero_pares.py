num =  int(input("Numero: "))
lista = []
while num>0:
    lista.append(num)
    num =  int(input("Numero: "))

print("Maximo:  %d"  % max(lista))

for elemento in lista:
    if elemento % 2 == 0:
        print(elemento)

#Si le introduces un numero negativo te muestra los numeros pares