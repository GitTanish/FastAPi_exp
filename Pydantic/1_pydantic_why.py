def insert(name:str,age:int):
# type annotation is still not type enforcement


    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print('Inserted into Database')
    else:
        raise TypeError('Incorrect data type')

def update(name:str,age:int):
# type annotation is still not type enforcement
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print('updated')
    else:
        raise TypeError('Incorrect data type')


insert('Doof',42)
