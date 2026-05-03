import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("finance.db")
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS finance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                amount INTEGER,
                type TEXT,
                category TEXT,
                date TEXT
            )
        """)
        self.conn.commit()

    def add_data(self, data):
        self.conn.execute("""
            INSERT INTO finance (title, amount, type, category, date)
            VALUES (?, ?, ?, ?, ?)
        """, data)
        self.conn.commit()

    def get_data(self):
        return self.conn.execute("SELECT * FROM finance ORDER BY date ASC").fetchall()

    def update_data(self, data_id, data):
        self.conn.execute("""
            UPDATE finance
            SET title=?, amount=?, type=?, category=?, date=?
            WHERE id=?
        """, (*data, data_id))
        self.conn.commit()

    def delete_data(self, data_id):
        self.conn.execute("DELETE FROM finance WHERE id=?", (data_id,))
        self.conn.commit()