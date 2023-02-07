import random

#Crear tupla
options = ('piedra', 'papel', 'tijera')

user_option = input('Piedra, papel o tijera => ')
user_option = user_option.lower()
# Verificar si un elemento está en una tupla
if not user_option in options:
    print('Esa opcion no es valida')
# Seleccion aleatoria para computer
computer_option = random.choice(options)

print('User option => ', user_option)
print('Computer option => ', computer_option)

if user_option == computer_option:
    print('Empate')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra gana a tijera')
        print('User ganó')
    else:
        print('Papel gana a piedra')
        print('Computer ganó')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel le gana a piedra')
        print('User ganó')
    else:
        print('tijera le gana a papel')
        print('computer ganó')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera le gana a piedra')
        print('user ganó')
    else:
        print('piedra le gana a papel')
        print('computer ganó')