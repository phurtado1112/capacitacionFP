### Módulos ###

import module

module.sum_two_values(2, 3)

module.print_value('Hola desde el módulo')

print('======================================')

from module import sum_two_values, print_value

sum_two_values(4, 5)
print_value('Cualquier cosa')

print('======================================')

import math

print(math.pi)
print(math.pow(2, 3))

from math import pi as PI_VALUE

print(PI_VALUE)