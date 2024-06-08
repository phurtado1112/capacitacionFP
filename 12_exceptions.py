### Exception handling ###

number_1 = 5
number_2 = 1

number_2 = '5'

#number_2 = False

## try - except

try:
  print(number_1 + number_2)
  print('No se ha producido un error')
except:
  # Se ejecuta si se produce una excepción
  print('Se ha producido un error')

print('==================================')

## try - except - else

try:
  print(number_1 + number_2)
  print('No se ha producido un error')
except:
  print('Se ha producido un error')
else:
  # Se ejecuta si NO se produce una excepción
  print('La ejecución continua correctamente en else')

print('==================================')

## try - except - else - finally

try:
  print(number_1 + number_2)
  print('No se ha producido un error')
except:
  print('Se ha producido un error')
else:
  # Se ejecuta si NO se produce una excepción
  print('La ejecución continua correctamente en else')
finally:
  # Se ejecuta siempre
  print('La ejecución continua en finally')

print('==================================')

## try - except de tipo

try:
  print(number_1 + number_2)
  print('No se ha producido un error')
except TypeError:
  # Se ejecuta si se produce una excepción
  print('Se ha producido un error')

print('==================================')

## try - except de tipo

try:
  print(number_1 + number_2)
  print('No se ha producido un error')
except TypeError:
  # Se ejecuta si se produce una excepción
  print('Se ha producido un error tipo')
except ValueError:
  # Se ejecuta si se produce una excepción
  print('Se ha producido un error value')

print('==================================')

## try - except de tipo

try:
  print(number_1 + number_2)
  print('No se ha producido un error')
except TypeError as error:
  # Se ejecuta si se produce una excepción
  print('Se ha producido un error tipo')
  print(error)
# except ValueError:
  # Se ejecuta si se produce una excepción
  # print('Se ha producido un error value')

print('==================================')

## try - except de tipo

try:
  print(number_1 + number_2)
  print('No se ha producido un error')
except ValueError as error:
  # Se ejecuta si se produce una excepción
  print('Se ha producido un error valor')
  print(error)
except Exception as exception:
  # Se ejecuta si se produce una excepción
  print('Se ha producido otro error')
  print(exception)

print('==================================')