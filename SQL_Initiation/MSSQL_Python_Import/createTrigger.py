import pyodbc
import conf

def create_trigger(conn):
    cursor = conn.cursor()

    trigger_sql = """
    CREATE TRIGGER trg_AuditUpdateEmploye
    ON webapp_employe
    AFTER UPDATE
    AS
    BEGIN
        INSERT INTO webapp_auditemploye (IdEmploye, AncienEtat, NouvelEtat, DateHeureModification)
        SELECT 
            i.IdEmploye, 
            d.Etat AS AncienEtat, 
            i.Etat AS NouvelEtat, 
            GETDATE()
        FROM 
            inserted i
        INNER JOIN 
            deleted d ON i.IdEmploye = d.IdEmploye
        WHERE 
            i.Etat <> d.Etat;
    END;
    """

    cursor.execute(trigger_sql)
    conn.commit()
    print("Trigger 'trg_AuditUpdateEmploye' created successfully.")

try:
    # Establish a connection to the SQL Server database
    with pyodbc.connect(conf.conn_str) as conn:
        print("Successfully connected to SQL Server")

        # Call the function to create the trigger
        create_trigger(conn)

        print("Trigger created successfully.")

except Exception as e:
    print("Error: ", e)
