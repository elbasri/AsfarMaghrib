import pyodbc
import conf

def delete_trigger(conn, trigger_name):
    cursor = conn.cursor()
    
    # Check if the trigger exists
    cursor.execute(f"IF OBJECT_ID(N'{trigger_name}', 'TR') IS NOT NULL DROP TRIGGER {trigger_name};")
    conn.commit()
    print(f"Trigger '{trigger_name}' deleted successfully.")

try:
    # Establish a connection to the SQL Server database
    with pyodbc.connect(conf.conn_str) as conn:
        print("Successfully connected to SQL Server")

        # Specify the name of the trigger to delete
        trigger_name = "trg_AuditUpdateEmploye"

        # Call the function to delete the trigger
        delete_trigger(conn, trigger_name)

        print("Trigger deleted successfully.")

except Exception as e:
    print("Error: ", e)
