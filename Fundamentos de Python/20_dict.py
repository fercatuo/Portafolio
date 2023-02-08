person = {
    'name': 'Fer',
    'last_name': 'Catú',
    'langs': ['python', 'javascript'],
    'age': 21
}

print(person)

# Cambiar un valor del dict
person['name'] = 'Allen'
person['age'] += 8
person['langs'].append('rust')
print(person)

# Eliminar un atributo
del person['last_name']
person.pop('age')
print(person)

print('Items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())