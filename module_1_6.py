my_dict = {'Dima': 1987, 'Valya': 2004, 'Anna': 2008}
print(my_dict.get('Dima'))
print(my_dict.get('Lori'))
my_dict.update({'Kolya': 1992, 'John': 1874})
del my_dict['John']
print(my_dict)

my_set = {0, 4, 4, 'Banana', 24.43546,19,(8, 2, 1.2)}
print(my_set)
my_set.update({'car', 58})
my_set.discard(24.43546)
print(my_set)