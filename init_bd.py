#!/usr/bin/env python
import sqlite3
import pandas as pd
import os

# CONFIGURACIÓN
TSV_FILE = "historia.export.all.tsv"
DB_FILE = "historia.db"  
TABLE_NAME = "fuentes_historicas"


# CARGAR EL ARCHIVO TSV
if not os.path.exists(TSV_FILE):
    raise FileNotFoundError(f" No se encontró el archivo {TSV_FILE}")

print(f" Cargando datos desde '{TSV_FILE}'...")
df = pd.read_csv(TSV_FILE, sep="\t", encoding="utf-8").fillna("")

# Normalizar nombres de columnas (por si vienen con espacios o acentos)
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# Mostrar resumen
print(f"Archivo cargado: {len(df):,} filas, {len(df.columns)} columnas")
print(f"Columnas detectadas: {list(df.columns)}")


# CREAR BASE DE DATOS SQLITE
conn = sqlite3.connect(DB_FILE)
df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
conn.close()

print(f"Base de datos '{DB_FILE}' creada correctamente con la tabla '{TABLE_NAME}'.")
