import pyodbc
import conf

def describe_table(table_name, conn):
    cursor = conn.cursor()

    query = f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}';"
    cursor.execute(query)

    columns = cursor.fetchall()

    # Print the columns of the table
    print(f"Columns of table '{table_name}':")
    for column in columns:
        print(column.COLUMN_NAME, column.DATA_TYPE)

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("Connected to SQL Server")

        # Describe the 'webapp_conduit' table
        #describe_table('webapp_conduit', conn)

        # Describe the 'webapp_employe' table
        describe_table('webapp_conduit', conn)

except Exception as e:
    print("Error: ", e)
