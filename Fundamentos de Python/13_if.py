# Solo se va a ejecutar si es verdadera
if True:
    print('Deberia ejecutarse')

# Nunca se va a ejecutar si es falso
if False:
    print('Nunca se ejecuta')

'''
pet = input('Ingresa tu mascota favorita => ')

if pet == 'gato':
    print('Tienes buen gusto')

if pet == 'perro':
    print('No te vaya a morder')
'''
'''
stock = int(input('Ingrese el stock '))

if stock >= 100 and stock <= 1000:
    print (f'El stock ingresado es correcto {stock}')
else:
    print(f'{stock} no es un Stock valido')
'''

pet = input('Ingresa tu mascota favorita => ')

if pet == 'gato':
    print('Tienes buen gusto')
elif pet == 'perro':
    print('No te vaya a morder')
elif pet == 'pez':
    print(f'{pet} es lo maximo')
else:
    print('No tienes una mascota interesante')

# Programa que evalue si es par o impar

numero = int(input(' Ingrea un numero => '))

if numero % 2 == 0:
    print('Par')
if numero % 2 == 1:
    print('Impar')

# Otra solucion
number = int(input('Ingrese un numero => '))

result = number % 2

if(result == 0):
    print('Es par')
else:
    print('Es impar')