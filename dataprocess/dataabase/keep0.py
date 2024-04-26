import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="test",
    password="test",
    database="test"
)
cursor = connection.cursor()
table_name = "companyplaced"
cursor.execute(f"DESCRIBE {table_name}")
columns = [column[0] for column in cursor.fetchall()]
exclude_columns = ["selected", "company_id"]
for column in columns:
    if column not in exclude_columns:
        update_query = f"UPDATE {table_name} SET `{column}` = 0;"
        cursor.execute(update_query)
connection.commit()
connection.close()
print("All values in all columns have been set to 0.")
