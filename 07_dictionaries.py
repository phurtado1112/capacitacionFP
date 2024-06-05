### DICTIONARIES ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

print('=========================================')

my_other_dict = {'Nombre':'Pablo', 'Apellido':'Pablo', 'Edad':'60', 1:'Python'} # Relación clave valor

my_dict = {'Nombre':'Pablo', 'Apellido':'Pablo', 'Edad':'60', 'Lenguajes':{'Python', 'PHP', 'Java'}, 1:1.65} 
print(my_other_dict)

print(my_dict)
print(my_other_dict)

print('=========================================')

print('my_dict logitud ' + str(len(my_dict)))
print('my_0ther_dict logitud ' + str(len(my_other_dict)))

print('=========================================')

print('Mi nombre es: ' + my_dict['Nombre'])

print('Mi edad es de: ' + my_dict['Edad'])

print('=========================================')

my_dict['Calle'] = '2da calle'

print(my_dict)

print('=========================================')

del my_dict['Calle']

print(my_dict)

print('=========================================')

print('Pablo' in my_dict) # no existe ==> False
print('Nombre' in my_dict) # si aparece ==> True

print('=========================================')

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(('Nombre', 1))) # Crea un nuevo diccionario con las claves dadas

print('=========================================')

my_new_dict = dict.fromkeys(('Nombre', 'Apellido', 1))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

print('=========================================')

my_values = my_new_dict.values()
print(my_values)

my_new_values = my_dict.values()
print(my_new_values)

print(tuple(my_other_dict))
print(set(my_other_dict))