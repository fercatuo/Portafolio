x = 3.3
print(x)

y = 1.1 +2.2
print(y)

# Trasnformamos y a un String para que quita la presicion decimal
# Pasamos la variable y definimos la precision decimal
y_str = format(y, ".2g")
# Ahora ya no es un int es str
print('str => ', y_str)
# Para realizar la comparacion, tambien debemos convertir el otro valor 'x'
print(y_str == str(x))

print('* *' * 10)
# Forma matemática
print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance)
