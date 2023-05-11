# Iteraciones y ciclos en Python

Principales Definiciones:

## Iterable

Es el nombre que recibe un conjunto de elementos.Algunos ejemplos de iterables incorporados en Python incluyen:

-   Listas
-   Tuplas
-   Cadenas de caracteres (strings)
-   Conjuntos (sets)
-   Diccionarios

Los iterables se utilizan extensamente en la programación de Python y se usan con frecuencia en bucles y otras operaciones relacionadas con la iteración.

Para iterar sobre un iterable en Python, se puede utilizar un bucle for o un bucle while. Por ejemplo:

    # iterar sobre una lista 
    mi_lista = [1, 2, 3] 
    for elemento in mi_lista:
        print(elemento)
        
    # iterar sobre una cadena de caracteres (string) 
    mi_cadena = "¡Hola, mundo!"  
    for caracter in mi_cadena: 
	    print(caracter) 
	    
	 # iterar sobre un diccionario 
	 mi_diccionario = {"a": 1, "b": 2, "c": 3} for clave, valor in 
	 mi_diccionario.items(): print(clave, valor)

# Iteraciones y ciclos en Python

Principales Definiciones:

## Iterable

Es el nombre que recibe un conjunto de elementos.Algunos ejemplos de iterables incorporados en Python incluyen:

 1. Son conjuntos de elementos
 2. Permiten retornar elementos que los componen
 3. se pueden recorrer usando ciclos
 4. Incluyen string, lists, tuple, dict, sets

## Iteradores

En python hay dos funciones nativas(builtins) que nos permiten crear iteradores sin necesidad de usar un ciclo

### iter()
Recibe el objeto iterable, crea un iterador y permite recorrerlo
### next()
Recibe el iterador creado, y cada vez que se invoca retorna el elemento siguiente en el iterable.

## Ejemplo en python 

    numeros = [1, 2, 3]
    iterador = iter(numeros)
    print(iterador)
    print(type(iterador))
	# imprimir el **siguiente** elemento en el **iterador** 
    print(next(iterador))

 - Cuando se intenta llamar al siguiente elemento usando next() y es el último, se genera un error. No es muy común ver iteradores en el código

iter: la función iter se usa como base para crear la siguientes: zip, map y filter

