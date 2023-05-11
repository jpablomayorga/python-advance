def get_area(side, *args, **kwargs):
    """    
    calculate the area of ​​a square from the measure of one of its sides
    """
    print('hello')
    print(side)
    print('args: ', *args)
    print(type(args))  

    for item in kwargs.items():
        print(item)
    
    for arg in args:
        print(arg)

    # return side * side

def say_hello(*args):
    print('hello')


if __name__ == '__main__':
    get_area('sss', 3, 4, key1 ='hello', key2='juan')
    say_hello(5)

"""
conclusiones:
1. las funciones pueden contener parametros en su definición ademas de args(argumentos) y kwars(key words arguments)
2. los *args son posicionales, variables y se pueden acceder desde la función como una tupla
3. los **kwargs son de typo clave valor y se acceden como un diccionario de python
4. los parametros pueden tener valor por defecto
5. las funciones pueden o no tener parametros y pueden o no retornar valores
6. las funciones se definen como un bloque de código hecho para hacer una tarea especifica, cuidado con ser tan extenso
"""




