'''
    Crea un ciclo infinito
while True:
    print('se ejecuto')

counter = 0

while counter < 10000:
    counter += 1
    print(counter)
    
print(time.process_time())   

# Rompemos el ciclo con break
counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break
''' 

import time


counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)
    
print('Time ejecution:', time.process_time())