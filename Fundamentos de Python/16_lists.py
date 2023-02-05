numbers = [1, 2, 3, 3]
print(numbers)
print(type(numbers))

tasks = ['make dishes', 'play videogames']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])

text = 'hola'
# text[0] ='W'
# Py no puede modificar un str disctamente
# Pero en una lista si la puede reemplazar

tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3])
print(True in types)
print('hola' in types)