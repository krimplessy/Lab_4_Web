import pandas as pd

def get_reader(conn):
    return pd.read_sql("SELECT * FROM reader", conn)

def get_book_reader(conn, reader_id):
    return pd.read_sql('''SELECT title AS Название, author_name AS Авторы, borrow_date AS Дата_выдачи, return_date AS Дата_сдачи
                        FROM reader JOIN book_reader ON reader.reader_id = book_reader.reader_id 
                        JOIN book ON book_reader.book_id = book.book_id
                        JOIN book_author ON book.book_id = book_author.book_id
                        JOIN author ON book_author.author_id = author.author_id
                        WHERE reader.reader_id == :reader_id
                       ''', conn, params = {"reader_id": reader_id})