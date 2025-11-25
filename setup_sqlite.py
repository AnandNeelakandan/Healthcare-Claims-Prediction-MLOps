import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "claims.db")

CSV_DIR = os.path.join(BASE_DIR, "NewDB")

def create_sqlite_db():
    conn = sqlite3.connect(DB_PATH)

    # Load CSVs
    claims = pd.read_csv(os.path.join(CSV_DIR, "claims.csv"))
    members = pd.read_csv(os.path.join(CSV_DIR, "members.csv"))
    providers = pd.read_csv(os.path.join(CSV_DIR, "providers.csv"))

    # Store them as SQLite tables
    claims.to_sql("claims", conn, if_exists="replace", index=False)
    members.to_sql("members", conn, if_exists="replace", index=False)
    providers.to_sql("providers", conn, if_exists="replace", index=False)

    conn.close()
    print("SQLite database created successfully at:", DB_PATH)


if __name__ == "__main__":
    create_sqlite_db()