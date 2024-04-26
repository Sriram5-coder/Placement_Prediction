import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="test",
    password="test",
    database="test"
)
cursor = connection.cursor()
column_to_keep = "selected"
value_to_keep = "value"
table_name = "placed"
cursor.execute(f"DESCRIBE {table_name}")
columns = [column[0] for column in cursor.fetchall()]
for column in columns:
    if column != column_to_keep:
        update_query = f"UPDATE {table_name} SET {column} = NULL WHERE {column_to_keep} != %s"
        cursor.execute(update_query, (value_to_keep,))
connection.commit()
connection.close()
print(f"All values in all columns except {column_to_keep} have been emptied except for rows where {column_to_keep} equals {value_to_keep}.")
