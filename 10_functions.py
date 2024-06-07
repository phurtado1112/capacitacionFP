### Funciones ###

def my_function():
  print('Esto es una función')

my_function()

print('==================================')

def sum_two_values(first_value, second_value):
  print(first_value + second_value)

sum_two_values(5, 8)
sum_two_values('5', '8')
sum_two_values(5.1, 8.1)

print('==================================')

def sum_two_values_with_return(first_value, second_value):
  return first_value + second_value

my_result = sum_two_values_with_return(10, 15)

print(my_result)

print('==================================')

def print_name(name, surname):
  print(f'{name} {surname}')

print_name('Pablo', 'Hurtado')

print('==================================')

def print_name_with_default(name, surname, alias='pelón'):
  print(f'{name} {surname} {alias}')

print_name_with_default('Pablo', 'Hurtado')
print_name_with_default('Pablo', 'Hurtado', 'phurtado')

print('==================================')

def print_texts(text):
  print(text)

print_texts('Hola')

def print_texts(*texts):
  print(texts)

print_texts('Hola', 'Pablo', 'Hurtado')
print_texts('Hola')

def print_texts_whith_iteration(*texts):
  for text in texts:
    print(text)

print_texts_whith_iteration('Hola', 'Pablo', 'Hurtado')

def print_texts_whith_iteration_to_upper(*texts):
  for text in texts:
    print(text.upper())

print_texts_whith_iteration_to_upper('Hola', 'Pablo', 'Hurtado')