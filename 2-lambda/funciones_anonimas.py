# multiplicacion de un numero por 2

a = lambda x: x * 2
# la variable a almacena un objeto de tipo function
print(type(a))

# se puede llamar la función por medio del objeto enviando el argumento de la función
print(a(35))

print(a)

suma = lambda  x, y: x + y
# funcion lambda de varios argumentos
print(suma(2,45))

# las funciones lambda tambien pueden usar kwargs y args
suma2 = lambda *args, **kwargs: sum(args) + sum(kwargs.values())
print(f'suma con args y kwargs: {suma2(1, 2, 3, a=4, b=5)}')


