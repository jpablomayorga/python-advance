def use_kwargs(grado, *args, **kwargs):
    print(type(grado)) 
    print(grado) 


    print('type args: ', type(args))
    print(args)

    for arg in args:
        print(f'arg : {arg}')

    print('type kwargs: ', type(kwargs))
    print(kwargs)

    for key, value in kwargs.items():
        print(f'clave : {key}, valor: {value}')



if __name__ == '__main__':
    use_kwargs('sexto', 6, True, name = 'Paco', apellido="botello", edad=31)

"""
conclusiones
1. el oreden de envion de argumentos va así: 1. parametros inciales, 2.*args, 3. **kwargs

"""