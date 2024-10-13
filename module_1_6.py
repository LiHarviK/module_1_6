my_dict = {'KFU':12345, 'KAI':54321}
print(my_dict)

print('Ваш номер:', my_dict['KFU'])

my_dict.update({'XAXAXA':1357, 'AXAXA':2468})
del my_dict['KFU']
print(my_dict)

my_set = {'Hello', 1, (1, 2, 3)}
print('Множество:', my_set)
my_set.add('str')
my_set.add('int')
my_set.discard(1)
print('Изменённое множество:', my_set)