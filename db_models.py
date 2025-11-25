from database import get_connection

def get_claim_by_id(claim_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM claims WHERE claim_id = ?", (claim_id,))
        result = cursor.fetchone()
        return dict(result) if result else None
    finally:
        cursor.close()
        conn.close()


def get_member_by_id(member_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM members WHERE member_id = ?", (member_id,))
        result = cursor.fetchone()
        return dict(result) if result else None
    finally:
        cursor.close()
        conn.close()


def get_provider_by_npi(provider_npi):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM providers WHERE provider_npi = ?", (provider_npi,))
        result = cursor.fetchone()
        return dict(result) if result else None
    finally:
        cursor.close()
        conn.close()