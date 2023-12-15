import pandas as pd

def get_author(con):
    return pd.read_sql("SELECT * FROM author", con)

def get_genre(con):
    return pd.read_sql("SELECT * FROM genre", con) 

def get_clients(con, author_name, genre):
    return pd.read_sql('''
                        SELECT DISTINCT client.name_client AS Имя_клиента
                        FROM client, buy, book, author, buy_book, genre
                        WHERE client.client_id = buy.client_id AND buy.buy_id = buy_book.buy_id AND
                        buy_book.book_id = book.book_id AND book.author_id = author.author_id AND author.name_author = :p_author AND
                        book.genre_id = genre.genre_id AND genre.name_genre = :p_genre
                        ORDER BY Имя_клиента DESC
                    ''', con, params={"p_author": author_name, "p_genre": genre})