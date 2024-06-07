### Bucles o ciclos ###

## While ##

my_condition = 0

while my_condition < 10:
  print(my_condition)
  my_condition += 1
else:# Es opcional
  print('Ya no cumple la condición')

print('==================================')

while my_condition < 20:
  my_condition += 1
  if my_condition == 15:
    print('El valor es 15')
  
  print(my_condition)


print('Sale del while')

print('==================================')

my_condition = 10

while my_condition < 20:
  my_condition += 1
  if my_condition == 15:
    print('Se detiene la ejecución')
    break 
  print(my_condition)


print('Sale del while')

print('==================================')

## For

my_list = [60, 35, 24, 62, 52, 30, 30, 17]

for element in my_list:
  print('El valor del elemento es: ' + str(element))

print('==================================')

my_tuple = (60, 1.65, 'Pablo', 'Hurtado')

my_set = {'Pablo', 'Hurtado', 60}

my_dict = {'Nombre':'Pablo', 'Apellido':'Hurtado', 'Edad':'60', 'Lenguajes':{'Python', 'PHP', 'Java'}, 1:1.65} 

for element in my_tuple:
  print('El valor del elemento en la tupla es: ' + str(element))

for element in my_set:
  print('El valor del elemento en el set es: ' + str(element))

for element in my_dict: # Imprime las keys
  print('El valor de la llave en el diccionario es: ' + str(element))

for element in my_dict.values(): # Imprime los valores
  print('El valor del valor en el diccionario es: ' + str(element))
else:
  print('El bucle for ha terminado')

for element in my_dict: # Imprime las keys
  print('El valor de la llave en el diccionario es: ' + str(element))
  if  element == 'Edad':
    break
  print('Se ejecuta')
else:
  print('Finaliza el for')

print('Sale del for')