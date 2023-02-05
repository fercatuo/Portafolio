text = 'Ella sabe programar en Python'
# Verificar si un subtexto o caracter esta en un string
print('JavaScript' in text)
print('Python' in text)

'''
if 'JS' in text:
    print('Elegiste bien')
else:
    print('Tambien elegiste bien')
'''
# analizar el tamaño de las cadenas 
size = len('amor     ')
print(size) 

# Mayusculas minusculas
print(text)
print(text.upper()) 
print(text.lower())

#contar cuantas veces aparece un dato
print(text.count('a'))

# cambia al tamaño contario las letras
print(text.swapcase())

# indica en que posicion esta la palabra
print(text.startswith('Ella'))
print(text.endswith('Rust'))

# Reemplazar
print(text.replace('Python', 'Go'))

text2 = 'este es un titulo'
print(text2)
# Convierte la primer caracter en Mayuscula
print(text2.capitalize())

# pone el inicio de cada palabra en mayuscula
print(text2.title())

# indica si un texto es un digito
print('28255'.isdigit())