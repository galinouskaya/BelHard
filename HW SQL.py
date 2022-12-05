import sqlite3

conn = sqlite3.connect('HW.sqlite3')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (24),
    email VARCHAR (24) UNIQUE
    )
    ''')
conn.commit()
#
cur.execute('''
    CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (24) UNIQUE
    )
''')
conn.commit()
#
cur.execute('''
    CREATE TABLE IF NOT EXISTS statuses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) UNIQUE
    )
    ''')
conn.commit()
#
cur.execute('''
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    status_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES statuses (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    ''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR (36),
    description VARCHAR (140),
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE
    );
    ''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders (id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
    );
    ''')
conn.commit()

cur.executemany('''
    INSERT INTO users (name, email)
    VALUES (?, ?);
    ''', (('vasia', 'vasia@mail.ru'), ('masha', 'masha@mail.ru'), ('boris', 'boris@mail.ru')))
conn.commit()

cur.executemany('''
    INSERT INTO categories (name)
    VALUES (?);
    ''', ('set', 'roll', 'lunch', 'dessert'))
conn.commit()



