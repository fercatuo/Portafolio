user_option = input('Piedra, papel o tijera => ')
computer_option = 'piedra'

if user_option == computer_option:
    print('Empate')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra gana a tijera')
        print('User ganó')
    else:
        print('Papel gana a pidra')
        print('Computer ganó')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel le gana a pieddra')
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