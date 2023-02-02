# Py Cambia el valor de forma dinamica
name = "Fer"
print(type(name))
name = 7
print(type(name))

# Identifica que tipo de dato va a operar,
# los cuales deben ser del mismo tipo si no dara un erro

print("Fer " + " Catú")
print ( 10 + 20)

age = 4
# se debe tranformar el tipo de dato al mismo con el que se 
# desea concatenar

# Con la funcion format no será necesario cambiar de tipo de dato 
print(f"Allen tiene {age} meses")

print("Su edad es " + str(age))

age = input("Ingresa tu edad =>")
print(type(age))
# Transformamos el valor ingresado str a int
age = int(age)
age = age + 10
print(f"Tu edad en 10 años será: {age}")