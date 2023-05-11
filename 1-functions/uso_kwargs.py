def use_kwargs(**kwargs):
    print('type kwargs: ', type(kwargs))
    print(kwargs)

    for key, value in kwargs.items():
        print(f'clave : {key}, valor: {value}')



if __name__ == '__main__':
    use_kwargs(name = 'Paco', apellido="botello", edad=31)

"""
conclusiones
1. la funcion que define los **kwargs puede tomar argumentos de tipo clave-valor que se pueden procesar como un dict de python
2. **kwargs se puede llamar de cualquier forma, solo es una convención
"""