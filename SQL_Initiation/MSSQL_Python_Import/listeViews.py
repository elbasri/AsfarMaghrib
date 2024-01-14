import pyodbc
import conf

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("Connected to SQL Server")
        
        cursor = conn.cursor()

        query = """
        SELECT table_name
        FROM information_schema.views
        """
        cursor.execute(query)

        views = cursor.fetchall()

        print("List of views in the database:")
        for view in views:
            print(view[0])

except Exception as e:
    print("Error: ", e)
