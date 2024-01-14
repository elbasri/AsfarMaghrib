-- Création de la vue Chauffeur
CREATE VIEW Chauffeur AS
SELECT 
    webapp_Employe.IdEmploye, 
    webapp_Employe.Nom, 
    webapp_Employe.Prenom, 
    webapp_Employe.Nationalite, 
    webapp_Employe.CarteIdentite, 
    webapp_Employe.Phone, 
    webapp_Employe.Etat, 
    webapp_Conduit.Licence -- Supposons que cette colonne existe dans la table webapp_Conduit
FROM 
    webapp_Employe
JOIN 
    webapp_Conduit ON webapp_Employe.IdEmploye = webapp_Conduit.IdEmploye;

-- Création de la vue AgentGuichet
CREATE VIEW AgentGuichet AS
SELECT 
    webapp_Employe.IdEmploye, 
    webapp_Employe.Nom, 
    webapp_Employe.Prenom, 
    webapp_Employe.Nationalite, 
    webapp_Employe.CarteIdentite, 
    webapp_Employe.Phone, 
    webapp_Employe.Etat, 
    webapp_Vend.ZoneResponsabilite -- Supposons que cette colonne existe dans la table webapp_Vend
FROM 
    webapp_Employe
JOIN 
    webapp_Vend ON webapp_Employe.IdEmploye = webapp_Vend.IdEmploye;
