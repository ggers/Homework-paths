# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def get_search_key():
    search_key = input("Введите ключ поиска")
    print(search_key)
    return(search_key)


    # ваша логика
    # 0 получить строку поиска
search_key = get_search_key()
    # 1. запросить текущую директорию
    # 2. перейти на уровень ниже чем запускаемый файл в директорию Миграции
    # 3. Циклом пройти все её файлы
for current_file in os.listdir(current_dir):
    with open(current_file) as sql_file:
        data = ???
    # 4. Если в файле есть строка поиска - сохранить его имя в промежуточный список
        if search_key in data:
            file_list.additem(current_file.path)
    # 5. запросить следующую строку поиска
search_key = get_search_key()
    # 6. циклом пройти по файлам, названия которых есть в архиве
    # 7. если в файле есть строка поиска - оставить элемент в списке - иначе удалить
    # 8. повторить пункт 5
