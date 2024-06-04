### STRINGS ###

my_string = 'Mi string'

my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + ' - ' + my_other_string)

my_new_line_string = 'Este es un String\ncon salto de línea'

print(my_new_line_string)

my_tab_string = '\tEste es un String con tabulación'

print(my_tab_string)

## FORMATEO ##
name = 'Pablo'
surname = 'Hurtado'
age = 60

print('====================================')

print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))

print('====================================')

print('Mi nombre es %s %s y mi edad es %d' %(name, surname,age))

print('====================================')

print(f'Mi nombre es {name} {surname} y mi edad es {age}')

## Desempaquetando caracteres de un string
language = 'Python'

a, b, c, d, e, f = language

print(a)
print(b)

## Recorte de un string ##

print('====================================')

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-3]
print(language_slice)

## Reverse ##
print('====================================')

language_reverse = language[::-1]
print(language_reverse)

## Functions ##
print('====================================')

print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count('t'))
print(language.isnumeric())
print(language.startswith('Py'))
print(language.startswith('py'))