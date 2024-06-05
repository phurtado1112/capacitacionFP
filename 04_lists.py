### Lists ###

my_list = list()

my_other_list = []

print(len(my_list))

my_list = [60, 35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [60, 1.65, 'Pablo', 'Hurtado']

print('====================================')

print(my_other_list)
print(len(my_other_list))

print(type(my_other_list))

print(my_other_list[0])

print(my_list + my_other_list)

my_other_list.append('PHD Systems')

print(my_other_list)

my_other_list.insert(3, 'MSc.')
print(my_other_list)

my_other_list.remove('MSc.')
print(my_other_list)

my_other_list.pop()
print(my_other_list)

del my_other_list[3]
print(my_other_list)

my_other_list.reverse()
print(my_other_list)

my_list.sort()
print(my_list)

my_other_list.clear()
print(my_other_list)