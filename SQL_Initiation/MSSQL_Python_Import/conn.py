import pyodbc
import conf

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("Connected to SQL Server")
        
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION")
        row = cursor.fetchone()
        print("SQL Server Version:", row[0])

except Exception as e:
    print("Error: ", e)
