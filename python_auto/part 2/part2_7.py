#Найти ТОП 2 дорогих товара
from operator import itemgetter
spisok = [{"Наименование": "Спички", "Цена": 1}, {"Наименование": "Лук", "Цена": 99}, {"Наименование": "Помидоры", "Цена": 97},{"Наименование": "Огурцы", "Цена": 55}, {"Наименование": "Кaпуста", "Цена": 66}]
spisok_sort = sorted(spisok, key=itemgetter('Цена'), reverse=True)
print(spisok_sort[0], spisok_sort[1])
