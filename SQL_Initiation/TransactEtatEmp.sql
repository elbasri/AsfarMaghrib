DECLARE @IdEmployeSpecifique INT;
SET @IdEmployeSpecifique = 123; -- Ici, 123 est un exemple pour le test

BEGIN TRANSACTION;

UPDATE webapp_Employe
SET Etat = 'Inactif'
WHERE IdEmploye = @IdEmployeSpecifique;

INSERT INTO AuditLog (TableModifiee, Operation, AncienneValeur, NouvelleValeur, DateHeureModification)
VALUES ('webapp_Employe', 'Mise à jour Etat', 'Actif', 'Inactif', GETDATE());

COMMIT;
