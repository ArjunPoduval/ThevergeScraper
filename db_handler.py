import sqlite3


conn = sqlite3.connect('mydatabase.db')

def create_db():
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ARTICLES
                    (id INTEGER PRIMARY KEY,
                    URL TEXT,
                    headline TEXT,
                    author TEXT,
                    date TEXT)''')

    conn.commit()
    print('SQLite database created successfully!')
    return conn


def insert_data(data):
    cursor = conn.cursor()
    new_data = []
    for i, d in enumerate(data):
        d_new = list(d)
        d_new.insert(0, i)   
        new_data.append(d_new)

    for data in new_data:
        print(data)
        cursor.execute('INSERT INTO ARTICLES VALUES (?,?,?,?,?)', data)
    conn.commit()
    conn.commit()
    return conn

def print_table():
    cursor = conn.execute('SELECT * from ARTICLES')
    for row in cursor:
        print(f'id = {row[0]}, url = {row[1]}, title = {row[2]}, author = {row[3]}, date = {row[4]}')

if __name__ == '__main__':
    create_db()
    