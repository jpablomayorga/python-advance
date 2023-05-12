numeros = [1, 2, 3]

iterator = iter(numeros)

print(iterator)

for i in range(len(numeros)):
    print(next(iterator))


"""
conclusiones:
1. los iteradores se pueden crear usando la funcion iter() sobre cualquier objeto que sea iterable
2. la funcion next retorna el siguiente elemento de un iterador
"""