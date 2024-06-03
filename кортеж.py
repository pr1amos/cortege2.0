immutable_var = 56, 8, 40, 'privet', 3.4, True
print(immutable_var)
# immutable_var[1] = 'no'
# print(immutable_var) # кортеж является неизменяемым типом данных,
#                      # для того, чтобы важные данные сохранились в неизменном виде

mutable_list = [56, 8, 40, 'privet', 3.4, True]
mutable_list[2] = 'yes'
print(mutable_list)