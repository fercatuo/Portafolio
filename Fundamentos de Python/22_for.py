
'''
for element in range(1, 20):
    print(element)
'''

# Recorrer estructuras
my_list = [23, 45, 67, 89, 43]

for element in my_list:
    print(element)

my_tuple = ('Fer', 'Allen', 'Santi')

for element in my_tuple:
    print(element)
# dictionary
product = {
    'name': 'camisa',
    'price': '100',
    'stock': 89
}
# al acceder a un dictionary nos da las llaver y con esas 
# mismas llaves podemos acceder a los valores
for key in product:
    print(key, '=>', product[key])

# con clave valor
for key, value in product.items():
    print(key, '=>', value)

# Lista de diccionarios
people = [
    {
        'name': 'fer',
        'age': 29
    },
    {
        'name': 'zule',
        'age': 45
    },
    {
        'name': 'Allen',
        'age': 4
    }
]

for person in people:
    print('name: ', person['name'])
