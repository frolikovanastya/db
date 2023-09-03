import sqlite3
def create_database():
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clients
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 first_name TEXT NOT NULL,
                 last_name TEXT NOT NULL,
                 email TEXT,
                 phone TEXT)''')
    conn.commit()
    conn.close()
def add_client(first_name, last_name, email=None, phone=None):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''INSERT INTO clients (first_name, last_name, email, phone)
                 VALUES (?, ?, ?, ?)''', (first_name, last_name, email, phone))
    conn.commit()
    conn.close()
def add_phone(client_id, phone):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''UPDATE clients SET phone = ? WHERE id = ?''', (phone, client_id))
    conn.commit()
    conn.close()
def update_client(client_id, first_name=None, last_name=None, email=None):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    if first_name:
        c.execute('''UPDATE clients SET first_name = ? WHERE id = ?''', (first_name, client_id))
    if last_name:
        c.execute('''UPDATE clients SET last_name = ? WHERE id = ?''', (last_name, client_id))
    if email:
        c.execute('''UPDATE clients SET email = ? WHERE id = ?''', (email, client_id))
    conn.commit()
    conn.close()
def delete_phone(client_id):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''UPDATE clients SET phone = NULL WHERE id = ?''', (client_id,))
    conn.commit()
    conn.close()

def delete_client(client_id):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''DELETE FROM clients WHERE id = ?''', (client_id,))
    conn.commit()
    conn.close()
def find_client(search_term):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM clients WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? OR phone LIKE ?''',
              (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
    result = c.fetchall()
    conn.close()
    return result

create_database()
add_client('John', 'Doe', 'john.doe@example.com', '123456789')
add_client('Jane', 'Smith', 'jane.smith@example.com')
add_phone(1, '987654321')
update_client(2, last_name='Johnson')
delete_phone(1)
delete_client(2)
print(find_client('John'))
