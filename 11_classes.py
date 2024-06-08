### Clases ####

class MyPerson:
  pass

print(MyPerson)
print(MyPerson())

print('======================================')

class Person:
  def __init__(self, name, surname) -> None:
    self.name = name
    self.surname = surname

my_person = Person('Pablo', 'Hurtado')

print(f'{my_person.name} {my_person.surname}')

print('======================================')

class Person1:
  def __init__(self, name, surname) -> None:
    self.full_name = f'{name} {surname}'

  def walk(self):
    print(f'{self.full_name} está caminando')

my_person_full = Person1('Pablo', 'Hurtado')

print(my_person_full.full_name)

my_person_full.walk()

print('======================================')

class Person2:
  def __init__(self, name, surname, alias = 'None') -> None:
    self.full_name = f'{name} {surname}'

  def walk(self):
    print(f'{self.full_name} 2 está caminando')

my_person_full = Person2('Pablo', 'Hurtado')

print(my_person_full.full_name)

my_person_full.walk()

