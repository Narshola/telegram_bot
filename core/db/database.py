import sqlite3

create = '''CREATE TABLE IF NOT EXISTS heroes(id INTEGER PRIMARY KEY, name VARCHAR, race VARCHAR, class VARCHAR, avatar VARCHAR)'''
insert = '''INSERT INTO heroes(id, name, race, class, avatar) VALUES (?, ?, ?, ?, ?)'''

def query(query, *args):
    conn = sqlite3.connect('heroes.sqlite')
    cursor = conn.cursor()
    cursor.execute(query, *args)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data

def get_data(from_user):
    conn = sqlite3.connect('heroes.sqlite')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM heroes WHERE id=?''', [from_user])
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data

if __name__ == '__main__':
    query(create)