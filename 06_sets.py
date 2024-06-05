### Sets ###

my_set = set()

print(type(my_set))

print('=====================================')

my_other_set = {}

print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {'Pablo', 'Hurtado', 60}

print(my_other_set)

print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('PHD Systems')

print(my_other_set) # No es una estructura Ordenada

my_other_set.add('PHD Systems') # NO permite valores repetidos

print(my_other_set)

print('Pablo' in my_other_set)
print('Pabli' in my_other_set)

my_other_set.remove('PHD Systems')

print(my_other_set)

# my_other_set.clear()

print(my_other_set)

my_set = {35, 50, 60}

my_list = list(my_set)

print(my_list)

print(my_other_set.union(my_set).union({'PHD Systems', 'Cacao POE'}))

print(my_set.difference(my_other_set))