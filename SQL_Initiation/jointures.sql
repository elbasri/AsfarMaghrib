SELECT 
    Vend.NumeroTicket,
    Ticket.NomClient,
    Ligne.Nom AS NomLigne,
    Ligne.Prix,
    Employe.Nom AS NomEmploye,
    Employe.Prenom AS PrenomEmploye,
    Vend.DateDepart,
    Vend.Heure
FROM 
    Vend
INNER JOIN 
    Ticket ON Vend.NumeroTicket = Ticket.NumeroTicket
INNER JOIN 
    Ligne ON Vend.NomLigne = Ligne.Nom
INNER JOIN 
    Employe ON Vend.IdEmploye = Employe.IdEmploye
WHERE 
    Vend.DateDepart BETWEEN '2022-01-01' AND '2022-12-31'
ORDER BY 
    Vend.DateDepart, Vend.Heure;
