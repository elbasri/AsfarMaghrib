import pyodbc
import conf
import os

conn_str = conf.conn_str

try:
    #with pyodbc.connect(conn_str, autocommit=True) as conn:
    #    print("Successfully connected to SQL Server")
    #    conn.execute("CREATE DATABASE AsfarMaghrib;")
    #    print("Database 'AsfarMaghrib' created successfully")

    with pyodbc.connect(conn_str + ";DATABASE=AsfarMaghrib", autocommit=True) as conn:
        
        script_path = os.path.join(os.path.dirname(__file__), '..', 'SchemaInitiale.sql')

        with open(script_path, 'r') as file:
            create_tables_script = file.read()

        conn.execute(create_tables_script)
        print("Tables created successfully in 'AsfarMaghrib'")

except Exception as e:
    print("Error: ", e)
