# Variables
# String
my_string_variable = 'My string variable'

print(my_string_variable)

# Integer
my_int_variable = 5

print(my_int_variable)

# Boolean
my_bool_variable = False

print(my_bool_variable)

# Concatenación de variable en una función print()
print(my_string_variable, my_int_variable, my_bool_variable)

# Function len()
print(len(my_string_variable))

# Variables en una sola línea
name, surname, age, alias = 'Pablo', 'Hurtado', 60, 'Pelón'

print('Me llamo', name, surname, 'Mi edad es:', age, 'y mi alias es:', alias)

# Functions to collect data form prompt

first_name = input('What is your name: ')
age = input('How old are you: ')

print(first_name)

print(age)

# or
print('Your name is',first_name, 'and you are', age, 'old')