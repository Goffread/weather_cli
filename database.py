import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="weather.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            windspeed REAL,
            created_at TEXT
            )
        """)
        self.conn.commit()

    def save_request(self, city, temperature, windspeed):
        now = datetime.now().isoformat()
        self.cursor.execute(
            "INSERT INTO requests (city, temperature, windspeed, created_at) VALUES (?, ?, ?, ?)", 
            (city, temperature, windspeed, now)
        )
        self.conn.commit()

    def get_history(self):
        self.cursor.execute("SELECT * FROM requests ORDER BY id DESC")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = Database()
    db.save_request("Москва", 23.5, 12.0)
    db.save_request("Казань", 19.0, 8.5)
    for row in db.get_history():
        print(row)
    db.close()
