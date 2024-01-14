import pyodbc
import conf

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("Connected to SQL Server")
        
        cursor = conn.cursor()

        query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_type = 'BASE TABLE'
        """
        cursor.execute(query)

        tables = cursor.fetchall()

        # Print the list of table names
        print("List of tables in the database:")
        for table in tables:
            print(table[0])

except Exception as e:
    print("Error: ", e)
