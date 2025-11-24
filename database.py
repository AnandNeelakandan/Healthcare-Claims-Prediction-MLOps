import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anandrandy@123",
        database="claimsprediction"
    )
    return connection
