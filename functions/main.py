def get_area(lado, *args, **kwargs):
    """    
    calculate the area of ​​a square from the measure of one of its sides
    """
    print('hello')
    print(lado)
    print('args: ', *args)
    print(type(args))

    for item in kwargs.items():
        print(item)


if __name__ == '__main__':
    get_area('sss', 3, 4, key1 ='hello', key2='juan')




