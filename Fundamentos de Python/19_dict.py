my_dict = {}
print(type(my_dict))

my_dict = {
    'avion': 'bla bla bla',
    'name': 'Fernando',
    'last_name': 'Catu Otzoy',
    'age': 21
}
print(my_dict)
print(len(my_dict))

# Podemos acceder a un valor por medio de su llave
print(my_dict['age'])
print(my_dict['last_name'])

# Get puede prevenir un error, ya que si un valor no esta en el
# diccionario nos lo va a indicar
print(my_dict.get('age'))
print(my_dict.get('pet'))

# validor si un valor esta en el diccionario
print('avion' in my_dict)
print('otroqueno' in my_dict)

