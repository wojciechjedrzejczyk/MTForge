import sqlite3
from pathlib import Path

class Database:
    def __init__(self):
        self.db_path = Path("data") / "mtforge.db"
        self.db_path.parent.mkdir(exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                score INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_user(self, username):
        try:
            self.conn.execute("INSERT INTO users (username) VALUES (?)",
                              (username,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass

    def update_score(self, username, score):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET score = ? WHERE username = ?",
                       (score, username))
        self.conn.commit()

    def get_user(self, username):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?",
                       (username,))
        return cursor.fetchone()

    def get_score(self, username):
        cursor = self.conn.cursor()
        cursor.execute("SELECT score FROM users WHERE username = ?",
                       (username,))
        row = cursor.fetchone()
        return row[0] if row else None
