import pyodbc
from config import settings

def get_sqlserver_connection():
    conn = pyodbc.connect(
        f"DRIVER={{SQL Server}};"
        f"SERVER={settings.SQLSERVER_HOST};"
        f"DATABASE={settings.SQLSERVER_DATABASE};"
        f"UID={settings.SQLSERVER_USER};"
        f"PWD={settings.SQLSERVER_PASSWORD};"
    )
    return conn


def fetch_data(query: str):
    conn = get_sqlserver_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


if __name__ == "__main__":
    conn = get_sqlserver_connection()
    print("Connection successful!")
    conn.close()