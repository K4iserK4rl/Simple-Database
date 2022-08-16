import sqlite3 as sql3
import pandas

connection = sql3.connect('test_database')
cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS products
               ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
               ''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS prices
               ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
               ''')

cursor.execute('''
               INSERT OR REPLACE INTO products (product_id, product_name)
                   VALUES
                   (1, 'Computer'),
                   (2, 'Printer'),
                   (3, 'Tablet'),
                   (4, 'Desk'),
                   (5, 'Chair')
               ''')

cursor.execute('''
               INSERT OR REPLACE INTO prices (product_id, price)
                   VALUES
                   (1, 800),
                   (2, 200),
                   (3, 300),
                   (4, 450),
                   (5, 150)
               ''')

cursor.execute('''
               SELECT
               a.product_name,
               b.price
               FROM products a
               LEFT JOIN prices b ON a.product_id = b.product_id
               ''')

connection.commit()

dataFrame = pandas.DataFrame(cursor.fetchall(), columns = ['product_name', 'price'])
print(dataFrame)
