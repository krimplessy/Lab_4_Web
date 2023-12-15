from jinja2 import Template
import sqlite3
from library_model import get_publisher, get_genre, get_reader, get_author, get_book_author, get_book, get_book_reader

# устанавливаем соединение с базой данных (базу данных взять из ЛР 1)
conn = sqlite3.connect("library.sqlite")

# выбираем записи из таблицы publisher
df_publisher = get_publisher(conn) 
df_genre = get_genre(conn) 
df_reader = get_reader(conn)
df_author = get_author(conn)
df_book_author = get_book_author(conn)
df_book = get_book(conn)
df_book_reader = get_book_reader(conn)

conn.close()

# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open("library_temp1.html", 'r', encoding ='utf-8-sig') 
html = f_template.read()
f_template.close()

# создаем объект-шаблон
template = Template(html)

# генерируем результат на основе шаблона
result_html = template.render(table_name1 = "publisher", relation1 = df_publisher, len = len,
                              table_name2 = "genre", relation2 = df_genre,
                              table_name3 = "reader", relation3 = df_reader,
                              table_name4 = "author", relation4 = df_author,
                              table_name5 = "book_author", relation5 = df_book_author,
                              table_name6 = "book", relation6 = df_book,
                              table_name7 = "book_reader", relation7 = df_book_reader)

#создаем файл для HTML-страницы
f = open('library.html', 'w', encoding ='utf-8-sig') 

# выводим сгенерированную страницу в файл 
f.write(result_html)
f.close()