### Condicionales ###
my_condition = False

if my_condition:
  print ('Se ejecuta el if')

print('Fuera del if')

print('==================================')

my_new_condition = 5 * 2

if my_new_condition == 10:
  print ('Se ejecuta el segundo if')
  

if my_new_condition >= 10:
  print ('Se ejecuta el tercer if')

print('Fuera de los if')

print('==================================')

my_other_condition = 10

if my_other_condition > 10:
  print ('El valor es mayor que 10')
else:
  print('El valor es menor o igual que 10')

print('==================================')

other_condition = 1

if other_condition > 10 and other_condition < 20:
  print('El valor es mayor que 10 y menor que 20')
elif other_condition == 1:
  print('Es igual a 1')
else:
  print('El valor es menor o igual que 10 o mayor que 20 o distinto de 25')

print('Continua fuera de los if')

print('==================================')

my_string = 'Mi cadena de texto'

if my_string:
  print('Mi cadena de texto no es vacía')

print('==================================')

my_string = ''

if not my_string:
  print('Mi cadena de texto es vacía')

print('Continua fuera de los if')