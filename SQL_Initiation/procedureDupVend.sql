CREATE PROCEDURE InsertVend
    @NumeroTicket INT,
    @NomLigneId NVARCHAR(255),
    @IdEmployeId NVARCHAR(255),
    @Heure TIME,
    @DateDepart DATETIME
AS
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM webapp_vend
        WHERE NumeroTicket = @NumeroTicket
          AND NomLigneId = @NomLigneId
          AND IdEmployeId = @IdEmployeId
          AND Heure = @Heure
          AND DateDepart = @DateDepart
    )
    BEGIN
        INSERT INTO webapp_vend (NumeroTicket, NomLigneId, IdEmployeId, Heure, DateDepart)
        VALUES (@NumeroTicket, @NomLigneId, @IdEmployeId, @Heure, @DateDepart)

        SELECT 'Insert successful' AS Result
    END
    ELSE
    BEGIN
        SELECT 'Duplicate entry. Insert failed.' AS Result
    END
END
