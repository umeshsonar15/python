# List
my_list = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE']
# first item
print(my_list[0]) # p
# third item
print(my_list[2]) # o
# fifth item
print(my_list[4]) # e
print(my_list[-1])
# elements from index 2 to index 4
print(my_list[2:5])

# Tuple
my_tuple = ("ABCD", 1, 'EFGH', 2, 'Python')
print(my_tuple)
print(my_tuple[0])
print(my_tuple[3])
print(my_tuple[-1])
print(my_tuple[1:4])
print(my_tuple[:3])
print(my_tuple[3:])
print((my_tuple) + (3, 'Programming', 4))
print(("ABCD",) * 3)
print(my_tuple.index(2))

# Dictionary
my_dict = {'name': 'Umesh', 'age': 21}
print(my_dict['name'])
print(my_dict.get('age'))
# update value
my_dict['age'] = 22
print(my_dict)
# add item
my_dict['address'] = 'Shirpur'
print(my_dict)
# remove item
print(my_dict.pop('address'))
