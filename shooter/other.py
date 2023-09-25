import pandas as pd

pd.DataFrame


dict_a = {'name': 'Artem'}

dict_b = {'name': 'Artem'}


print(dict_a == dict_b)
print(dict_a is dict_b)
print(id(dict_a))
print(id(dict_b))

int_a = 5
int_b = 5

print(int_a is int_b)
print(id(int_a))
print(id(int_b))

str_a = 'key'
str_b = 'key'

print(str_a == str_b)
print(str_a is str_b)
print(id(str_a))
print(id(str_b))
