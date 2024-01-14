CREATE TRIGGER trg_AuditUpdateEmploye
ON webapp_Employe
AFTER UPDATE
AS
BEGIN
    INSERT INTO AuditEmploye (IdEmploye, AncienEtat, NouvelEtat, DateHeureModification)
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
