import sqlite3

conn = sqlite3.connect('HW SQL new.sqlite3')
cur = conn.cursor()

cur.execute('''
     CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name VARCHAR (24),
     email VARCHAR (24) UNIQUE
     )
     ''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (24) UNIQUE NOT NULL
    )
''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS statuses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) UNIQUE NOT NULL
    )
    ''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (status_id) REFERENCES statuses (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    ''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR (36) NOT NULL,
    description VARCHAR (140),
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE
    );
    ''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
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
    ''', (('set',), ('roll',), ('lunch',), ('dessert',)))
conn.commit()

cur.executemany('''
    INSERT INTO products (title, description, category_id)
    VALUES (?, ?, ?)
    ''', (('santa set', '1171g/40p', '1'),
          ('philadelphia', '', '2'),
          ('monday', '', '3'),
          ('fruto muki', '220g/6p', '4')))
conn.commit()

cur.executemany('''
    INSERT INTO statuses (name)
    VALUES (?)
    ''', (('received',), ('collected',), ('on the way',), ('delivered',)))
conn.commit()

cur.executemany('''
    INSERT INTO orders (user_id, status_id)
    VALUES (?, ?)
    ''', (('2', '3'), ('1', '4'), ('3', '1')))
conn.commit()

cur.executemany('''
    INSERT INTO order_items (order_id, product_id)
    VALUES (?, ?)
    ''', (('2', '3'), ('3', '1'), ('1', '4'), ('1', '2'), ('1', '3')))
conn.commit()

