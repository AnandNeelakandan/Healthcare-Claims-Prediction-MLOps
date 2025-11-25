import sqlite3
import os

# Path to claims.db
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "claims.db")

def get_connection():
    return sqlite3.connect(DB_PATH)


# ------------- CLAIMS -------------
def get_claim_by_id(claim_id):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM claims WHERE ClaimID = ?", (claim_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        cursor.close()
        conn.close()


# ------------- MEMBERS -------------
def get_member_by_id(member_id):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM members WHERE MemberID = ?", (member_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        cursor.close()
        conn.close()


# ------------- PROVIDERS -------------
def get_provider_by_npi(provider_npi):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM providers WHERE ProviderNPI = ?", (provider_npi,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        cursor.close()
        conn.close()