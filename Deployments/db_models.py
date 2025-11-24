from database import get_connection

def get_claim_by_id(claim_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM claims WHERE ClaimID = %s", (claim_id,))
        result = cursor.fetchone()
        return result
    finally:
        try:
            cursor.fetchall()
        except:
            pass
        cursor.close()
        conn.close()


def get_member_by_id(member_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM members WHERE MemberID = %s", (member_id,))
        result = cursor.fetchone()
        return result
    finally:
        try:
            cursor.fetchall()
        except:
            pass
        cursor.close()
        conn.close()


def get_provider_by_npi(provider_npi):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM providers WHERE ProviderNPI = %s", (provider_npi,))
        result = cursor.fetchone()
        return result
    finally:
        try:
            cursor.fetchall()
        except:
            pass
        cursor.close()
        conn.close()