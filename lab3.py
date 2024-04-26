#!/usr/bin/env python3

import os
import cgi
import cgitb

# Увімкніть режим відлагодження CGI, щоб мати можливість бачити помилки
cgitb.enable()

# Визначте каталог, який ви хочете переглянути
directory = '/usr/lib/cgi-bin/'

# Отримайте список файлів у каталозі
file_list = os.listdir(directory)

# Повертає HTML-відповідь із списком файлів
print("Content-Type: text/html; charset=UTF-8")

print()  # Порожній рядок, що означає кінець заголовків HTTP

print("<html>")
print("<head><title>Список файлів</title></head>")
print("<body>")
print("<h1>Список файлів у каталозі</h1>")

print("<ul>")  # Початок списку
for file_name in file_list:
    print(f"<li>{file_name}</li>")  # Додати кожен файл у список
print("</ul>")  # Кінець списку

print("</body>")
print("</html>")

