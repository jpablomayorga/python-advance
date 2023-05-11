lista_numeros =[1,2,3,4,5,6,7,8]
# evalua si un numero es par o no
es_par = lambda n: n % 2 == 0

print(es_par(34))

# filter toma la condicion a evaluar y sobre que iterable hacerlo
lista_pares = list(filter(lambda n: n % 2 == 0, lista_numeros))
print(lista_pares)

print(lista_numeros)
# uso de map con lambda
doble_numeros = list(map(lambda x: x * 2, lista_numeros))
print(doble_numeros)