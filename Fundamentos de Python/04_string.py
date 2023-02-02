name = "Fernando"
last_name = "Catú"
age = 29
print(name)
print(last_name)

# Concatenar 

full_name = name + " " + last_name
print(full_name)

# comilla doble
quote = "I'm Fernando"
print(quote)

# comilla simple
quote2 = ' She said "Hello" '
print (quote2)

# format

template = "Hola mi nombre es: " + name + " y mi apellido es: " + last_name 
print("v1", template)

# La funcion format nos ayuda a reemplazar las llaver por el valor que le indiquemos
# en el orden que coloquemos en los parametros de la funcion irá reemplazando en las llaves
template = "Hola mi nombre es: {} y mi apellido es: {}".format(name, last_name)
print("v2", template)

# Esta es la forma mas utilizada por ser la mas sencilla de utilizar
template = f"Hola mi nombre es: {name} y mi apellido es: {last_name} y mi edad es: {age}"
print("v3", template)
