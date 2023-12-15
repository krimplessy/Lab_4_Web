from jinja2 import Template
import sqlite3
from store_model import get_clients, get_author, get_genre

con = sqlite3.connect("store.sqlite")

author_name = "Пастернак Б.Л."
genre = "Поэзия"

f_damp = open('store.db','r', encoding='utf-8-sig')
damp = f_damp.read()
f_damp.close()

con.executescript(damp)
con.commit()

df_author = get_author(con)
df_genre = get_genre(con)
df_clients = get_clients(con, author_name, genre)

con.close()

f_template = open("clients_templ.html", 'r', encoding ='utf-8-sig') 
html = f_template.read()
f_template.close()

template = Template(html)

result_html = template.render(clients = df_clients,
                              combo_box_au = df_author,
                              combo_box_g = df_genre,
                              name_author = author_name,
                              name_genre = genre,
                              len = len)

f = open('clients.html', 'w', encoding ='utf-8-sig')
f.write(result_html)
f.close()