from django.db import models

class Vehicules(models.Model):
    Plaque = models.CharField(max_length=7, primary_key=True)
    Marque = models.CharField(max_length=20, null=True)
    Place = models.IntegerField()
    Etat = models.CharField(max_length=20)

    def __str__(self):
        return f"Plaque: {self.Plaque} - Marque: {self.Marque} - Place: {self.Place} -Etat: {self.Etat}"

    class Meta:
        app_label = 'webapp'

class Ligne(models.Model):
    Nom = models.CharField(max_length=30, primary_key=True)
    Prix = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Heures = models.CharField(max_length=30)
    Interval = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.Nom} (Prix: {self.Prix} - Heures: {self.Heures} - Interval: {self.Interval}"

    class Meta:
        app_label = 'webapp'

class Employe(models.Model):
    IdEmploye = models.CharField(max_length=10, primary_key=True)
    Nom = models.CharField(max_length=20)
    Prenom = models.CharField(max_length=20)
    Nationalite = models.CharField(max_length=15, null=True)
    CarteIdentite = models.CharField(max_length=20, null=True)
    Phone = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    Etat = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Nom} {self.Prenom} - {self.CarteIdentite} (Tel: {self.Phone})"

    class Meta:
        app_label = 'webapp'


class Ticket(models.Model):
    NumeroTicket = models.BigIntegerField(primary_key=True)
    NomClient = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.NumeroTicket} (Client: {self.NomClient})"

    class Meta:
        app_label = 'webapp'

class Branche(models.Model):
    IdBranche = models.CharField(max_length=10, primary_key=True)
    Nom = models.CharField(max_length=20)
    Localisation = models.CharField(max_length=30, null=True)
    Etat = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.Nom} (Localisation: {self.Localisation})"

    class Meta:
        app_label = 'webapp'

class Service(models.Model):
    IdService = models.CharField(max_length=10, primary_key=True)
    NomService = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.NomService}"

    class Meta:
        app_label = 'webapp'

class Vend(models.Model):
    NumeroTicket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    NomLigne = models.ForeignKey(Ligne, on_delete=models.CASCADE)
    IdEmploye = models.ForeignKey(Employe, on_delete=models.CASCADE)
    Heure = models.CharField(max_length=15, verbose_name="Heure", null=False)
    DateDepart = models.DateTimeField(verbose_name="Date de départ", null=False)
    def __str__(self):
        return f"NumeroTicket: {self.NumeroTicket} - NomLigne: {self.NomLigne} - IdEmploye: {self.IdEmploye} - Heure: {self.Heure} - DateDepart: {self.DateDepart}"

    class Meta:
        unique_together = ('NumeroTicket', 'NomLigne', 'IdEmploye')
        app_label = 'webapp'

class Conduit(models.Model):
    IdEmploye = models.ForeignKey(Employe, on_delete=models.CASCADE)
    Plaque = models.ForeignKey(Vehicules, on_delete=models.CASCADE)
    NomLigne = models.ForeignKey(Ligne, on_delete=models.CASCADE)
    Date = models.DateTimeField()
    Heure = models.CharField(max_length=15)
    def __str__(self):
        return f"IdEmploye: {self.IdEmploye} - Plaque: {self.Plaque} - NomLigne: {self.NomLigne} - Date: {self.Date} - Heure: {self.Heure}"

    class Meta:
        unique_together = ('IdEmploye', 'Plaque', 'NomLigne', 'Date')
        app_label = 'webapp'

class Travaille(models.Model):
    IdEmploye = models.ForeignKey(Employe, on_delete=models.CASCADE)
    IdBranche = models.ForeignKey(Branche, on_delete=models.CASCADE)
    IdService = models.ForeignKey(Service, on_delete=models.CASCADE)
    Date = models.DateTimeField()
    Annee = models.IntegerField()
    def __str__(self):
        return f"IdEmploye: {self.IdEmploye} - IdBranche: {self.IdBranche} - IdService: {self.IdService} - Date: {self.Date}"

    class Meta:
        unique_together = ('IdEmploye', 'IdBranche', 'IdService', 'Date')
        app_label = 'webapp'

class ChauffeurView(models.Model):
    IdEmploye = models.CharField(max_length=10, primary_key=True)
    Nom = models.CharField(max_length=20)
    Prenom = models.CharField(max_length=20)
    Nationalite = models.CharField(max_length=15, null=True)
    CarteIdentite = models.CharField(max_length=20, null=True)
    Phone = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    Etat = models.CharField(max_length=20)
    Licence = models.CharField(max_length=15)

    class Meta:
        managed = False

class AgentGuichetView(models.Model):
    IdEmploye = models.CharField(max_length=10, primary_key=True)
    Nom = models.CharField(max_length=20)
    Prenom = models.CharField(max_length=20)
    Nationalite = models.CharField(max_length=15, null=True)
    CarteIdentite = models.CharField(max_length=20, null=True)
    Phone = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    Etat = models.CharField(max_length=20)
    ZoneResponsabilite = models.CharField(max_length=30)

    class Meta:
        managed = False

class AuditEmploye(models.Model):
    AuditId = models.AutoField(primary_key=True)
    IdEmploye = models.CharField(max_length=10)
    AncienEtat = models.CharField(max_length=20)
    NouvelEtat = models.CharField(max_length=20)
    DateHeureModification = models.DateTimeField()

    def __str__(self):
        return f'Audit ID: {self.AuditId}, Employee ID: {self.IdEmploye}, ' \
               f'Previous State: {self.AncienEtat}, New State: {self.NouvelEtat}, ' \
               f'Date and Time: {self.DateHeureModification}'
    
class CustomQueryData(models.Model):
    numero_ticket = models.IntegerField()
    nom_client = models.CharField(max_length=255)
    nom_ligne = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nom_employe = models.CharField(max_length=255)
    prenom_employe = models.CharField(max_length=255)
    date_depart = models.DateField()
    heure = models.TimeField()

    class Meta:
        managed = False