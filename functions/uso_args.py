def calula_perimetro(*args):
    """
    se calcula el perimetro de un poligono como la suma de sus lados
    """
    p = 0
    for arg in args:
        p += arg
    return p

if __name__ == '__main__':
    print(calula_perimetro(4,3,2,1))

"""
conclusiones
1. Los args son una tupla de elemntos variables
2. No se estan manejando los errores
"""