immutable_var = (1, 2, 'q', 't')
print(immutable_var)
#immutable_var[0] = 56
# print(immutable_var) # Операция по изменению кортеже не выполнилась из-зи того, что кортежи — это контейнеры, хранящие объекты в определенном порядке и как только мы его создали, значение какого-либо его элемента уже нельзя изменить.
mutable_list = [1, 2, 'd', 'e', 'pizza']
mutable_list[0] = 45
mutable_list.append('appel')
print(mutable_list)
