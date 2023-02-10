import random

#Crear tupla
options = ('piedra', 'papel', 'tijera')

# Cuantas veces ha ganado
computer_wins = 0
user_wins = 0

rounds = 1

while True: 

    print('*' * 10)
    print('ROUNDS: ', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    user_option = input('Piedra, papel o tijera => ')
    user_option = user_option.lower()

    rounds += 1 

    # Verificar si un elemento está en una tupla
    if not user_option in options:
        print('Esa opcion no es valida')
        continue
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
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('Computer ganó')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel le gana a piedra')
            print('User ganó')
            user_wins += 1
        else:
            print('tijera le gana a papel')
            print('computer ganó')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera le gana a piedra')
            print('user ganó')
            user_wins += 1
        else:
            print('piedra le gana a papel')
            print('computer ganó')
            computer_wins += 1
    if computer_wins == 2:
        print('El ganador es la computadora')
        break
    if computer_wins == 2:
        print('El ganador es la computadora')
        break