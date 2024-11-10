import sqlite3

# database setup is the following:
# users table holds email, pw, and user_id
# atms table holds user_id, atm_id
# transactions table holds atm_id transaction_id
# alerts table holds alert_id transaction_id

conn = sqlite3.connect('backend/database.db')
cursor = conn.cursor()

# create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    pw TEXT NOT NULL
)
''')

# create atms table
cursor.execute('''
CREATE TABLE IF NOT EXISTS atms (
    atm_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
''')

# create transactions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    atm_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (atm_id) REFERENCES atms (atm_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)            
)
''')

# create alerts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS alerts (
    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id INTEGER,
    atm_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (transaction_id) REFERENCES transactions (transaction_id),
    FOREIGN KEY (atm_id) REFERENCES atms (atm_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)      
)
''')


# commit and close
conn.commit()
conn.close()


