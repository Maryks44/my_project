# Дана строка, содержащая полное имя файла (например, C:\development\inside\test-project_management\inside\myfile.txt').
# Выделите из этой строки имя файла без расширения
path_file = input('Укажите путь до файла: ')
point = path_file.rfind('.')
slash = path_file.rfind('\\')
name = path_file[slash+1:point]
print(name)