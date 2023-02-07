'''
Métodos de las listas

append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
'''
number = [1, 2, 3, 4, 5]
number.pop(2)
print(number)
number[-1 ] = 10
print(number)

# insertó al final
number.append(700)
print(number)

# insertar al inicio
number.insert(0, 'h0la')
print(number)

# insertar en posicion 
number.insert(3, 'change')
print(number)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = number + tasks
print(new_list)

# preguntar en posicion esta un elemento 
index = new_list.index('todo 2')
print(index)
# cambiar el valor
new_list[index] = 'todo changed'
print(new_list)

new_list.remove('todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

string = ['re', 'ab', 'ed']
string.sort
print(string)

