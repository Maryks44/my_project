#Поменять местами самый большой и самый маленький элемент списка
lists = list(input('Укажите элементы списка: '))
max_index = lists.index(max(lists))
min_index = lists.index(min(lists))
lists[max_index], lists[min_index] = lists[min_index], lists[max_index]
print(lists)