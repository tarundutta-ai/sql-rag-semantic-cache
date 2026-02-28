from database import get_sqlserver_connection

def get_schema_metadata():
    conn = get_sqlserver_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        TABLE_NAME,
        COLUMN_NAME,
        DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    ORDER BY TABLE_NAME
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    schema_dict = {}

    for row in rows:
        table = row.TABLE_NAME
        column = row.COLUMN_NAME
        datatype = row.DATA_TYPE

        if table not in schema_dict:
            schema_dict[table] = []

        schema_dict[table].append(f"{column} ({datatype})")

    cursor.close()
    conn.close()

    schema_text = ""
    for table, columns in schema_dict.items():
        schema_text += f"\nTable: {table}\n"
        for col in columns:
            schema_text += f"  - {col}\n"

    return schema_text


