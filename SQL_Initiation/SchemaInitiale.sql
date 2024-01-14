-- Créer la table Véhicules 
CREATE TABLE Vehicules (
    Plaque NVARCHAR(7) PRIMARY KEY,
    Marque NVARCHAR(20) NULL,
    Place INT NOT NULL,
    Etat VARCHAR(20) NOT NULL
);

-- Créer la table Ligne 
CREATE TABLE Ligne (
    Nom VARCHAR(30) PRIMARY KEY,
    Prix MONEY NULL,
    Heures NVARCHAR(30) NOT NULL,
    Interval NVARCHAR(20) NOT NULL
);

-- Créer la table Employé
CREATE TABLE Employe (
    IdEmploye NVARCHAR(10) PRIMARY KEY,
    Nom VARCHAR(20) NOT NULL,
    Prenom VARCHAR(20) NOT NULL,
    Nationalite VARCHAR(15) NULL,
    CarteIdentite NVARCHAR(20) NULL,
    Phone NUMERIC(20) NULL,
    Etat VARCHAR(20) NOT NULL
);

-- Créer la table Ticket 
CREATE TABLE Ticket (
    NumeroTicket BIGINT PRIMARY KEY,
    NomClient VARCHAR(30) NOT NULL
);

-- Créer la table Branche 
CREATE TABLE Branche (
    IdBranche NVARCHAR(10) PRIMARY KEY,
    Nom VARCHAR(20) NOT NULL,
    Localisation VARCHAR(30) NULL,
    Etat VARCHAR(20) NOT NULL
);

-- Créer la table Service 
CREATE TABLE Service (
    IdService NVARCHAR(10) PRIMARY KEY,
    NomService VARCHAR(20) NOT NULL
);

-- Créer la table Vend
CREATE TABLE Vend (
    NumeroTicket BIGINT,
    NomLigne VARCHAR(30),
    IdEmploye NVARCHAR(10),
    Heure NVARCHAR(15) NOT NULL,
    DateDepart DATETIME NOT NULL,
    PRIMARY KEY (NumeroTicket, NomLigne, IdEmploye),
    FOREIGN KEY (NumeroTicket) REFERENCES Ticket(NumeroTicket),
    FOREIGN KEY (NomLigne) REFERENCES Ligne(Nom),
    FOREIGN KEY (IdEmploye) REFERENCES Employe(IdEmploye)
);

-- Créer la table Conduit
CREATE TABLE Conduit (
    IdEmploye NVARCHAR(10),
    Plaque NVARCHAR(7),
    NomLigne VARCHAR(30),
    Date DATETIME NOT NULL,
    Heure NVARCHAR(15) NOT NULL,
    PRIMARY KEY (IdEmploye, Plaque, NomLigne, Date),
    FOREIGN KEY (IdEmploye) REFERENCES Employe(IdEmploye),
    FOREIGN KEY (Plaque) REFERENCES Vehicules(Plaque),
    FOREIGN KEY (NomLigne) REFERENCES Ligne(Nom)
);

-- Créer la table Travaille
CREATE TABLE Travaille (
    IdEmploye NVARCHAR(10),
    IdBranche NVARCHAR(10),
    IdService NVARCHAR(10),
    Date DATETIME NOT NULL,
    Annee INT NOT NULL, -- Change NUMERIC(180) to INT
    PRIMARY KEY (IdEmploye, IdBranche, IdService, Date),
    FOREIGN KEY (IdEmploye) REFERENCES Employe(IdEmploye),
    FOREIGN KEY (IdBranche) REFERENCES Branche(IdBranche),
    FOREIGN KEY (IdService) REFERENCES Service(IdService)
);
