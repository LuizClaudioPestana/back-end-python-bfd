import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db" / "teste.db"

db_conection = sqlite3.connect(DB_PATH)

cursor = db_conection.cursor()

cursor.execute("""
               CREATE TABLE Registro (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     nome TEXT NOT NULL,
                     idade INTEGER,
                     cidade TEXT
                )
                """ 
                )
db_conection.commit()
db_conection.close()