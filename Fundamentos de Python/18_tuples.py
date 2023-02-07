# Tupla va entre parentesis
numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')

print(numbers)
# acceder al indice
print('0 => ', numbers[0])
print('0 => ', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD
# numbers.append(10)
print(numbers)
# numbers[1] = 'change'

# propiedades de tuplas
print(strings)
print(strings.index('zule'))
print(strings.count('nico'))

# Pasar una tupla a lista
my_list = list(strings)
print(my_list)
print(type(my_list))

# modificar elementos 
my_list[1] = 'juli'
print(my_list)

# Devolver la lista a tupla
my_tuple = tuple(my_list)
print(my_tuple)
