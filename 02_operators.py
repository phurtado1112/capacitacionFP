### Operadores ###
## Aritméticos ##
print(3 + 5)
print(3 - 5)
print(3 * 5)
print(3 / 5)

# Avanzados
print(3 % 5)
print(10 // 3)
print(3 ** 5)

# Texto
print('Hola ' + 'Python ' + '¿Qué tal?')

print('Hola ' + str(10)) # No se puede concatenar el número de forma directa es necesario el casting

print('HOLA ' * 3)

my_float = 2.5 * 2
print('Hola ' * int(my_float))

## Comparativos ##
# Con número

print('== Números ==')
print( )
print( 3 < 4)
print( 3 >= 4)
print( 3 <= 4)
print( 3 == 4)
print( 3 != 4)
print('=========================================')

# Con texto

print('== Texto ==')
print('2.1 ')
print('Hola' > 'Python') # lo hace por ordenación alfabética por ASCII
print('2.2 ')
print(len('Hola') > len('Python')) # lo hace por cantidad de caracteres
print('2.3 ')
print('Hola' < 'Python')
print('2.4 ')
print('Hola' >= 'Python')
print('2.5 ')
print('Hola' <= 'Python')
print('2.6 ')
print('Hola' == 'Python')
print('2.7 ')
print('Hola' != 'Python')
print('=========================================')

## Lógicos ##
print('3.1 ')
print(3 > 4 and 'Hola' > 'Python')
print('3.2 ')
print(3 > 4 or 'Hola' > 'Python')
print('3.3 ')
#print(3 > 4 not 'Hola' > 'Python')
print(not(3 > 4)) 