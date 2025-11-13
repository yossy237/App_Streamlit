import sqlite3
import pandas as pd

DB_PATH = "historia.db"

# Conectarse
conn = sqlite3.connect(DB_PATH)

# Mostrar tablas disponibles
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("📋 Tablas encontradas:\n", tables)

# Mostrar primeras filas
df = pd.read_sql_query("SELECT * FROM fuentes_historicas LIMIT 5;", conn)
print("\n Contenido inicial:\n", df)

conn.close()
