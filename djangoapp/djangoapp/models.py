from django.db import models

class Vehicules(models.Model):
    Plaque = models.CharField(max_length=7, primary_key=True)
    Marque = models.CharField(max_length=20, null=True)
    Place = models.IntegerField()
    Etat = models.CharField(max_length=20)
    class Meta:
        app_label = 'admin'

class Ligne(models.Model):
    Nom = models.CharField(max_length=30, primary_key=True)
    Prix = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Heures = models.CharField(max_length=30)
    Interval = models.CharField(max_length=20)
    class Meta:
        app_label = 'admin'

class Employe(models.Model):
    IdEmploye = models.CharField(max_length=10, primary_key=True)
    Nom = models.CharField(max_length=20)
    Prenom = models.CharField(max_length=20)
    Nationalite = models.CharField(max_length=15, null=True)
    CarteIdentite = models.CharField(max_length=20, null=True)
    Phone = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    Etat = models.CharField(max_length=20)
    class Meta:
        app_label = 'admin'

class Ticket(models.Model):
    NumeroTicket = models.BigIntegerField(primary_key=True)
    NomClient = models.CharField(max_length=30)
    class Meta:
        app_label = 'admin'

class Branche(models.Model):
    IdBranche = models.CharField(max_length=10, primary_key=True)
    Nom = models.CharField(max_length=20)
    Localisation = models.CharField(max_length=30, null=True)
    Etat = models.CharField(max_length=20)
    class Meta:
        app_label = 'admin'

class Service(models.Model):
    IdService = models.CharField(max_length=10, primary_key=True)
    NomService = models.CharField(max_length=20)

    class Meta:
        app_label = 'admin'

class Vend(models.Model):
    NumeroTicket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    NomLigne = models.ForeignKey(Ligne, on_delete=models.CASCADE)
    IdEmploye = models.ForeignKey(Employe, on_delete=models.CASCADE)
    Heure = models.CharField(max_length=15, verbose_name="Heure", null=False)
    DateDepart = models.DateTimeField(verbose_name="Date de départ", null=False)

    class Meta:
        unique_together = ('NumeroTicket', 'NomLigne', 'IdEmploye')
        app_label = 'admin'

class Conduit(models.Model):
    IdEmploye = models.ForeignKey(Employe, on_delete=models.CASCADE)
    Plaque = models.ForeignKey(Vehicules, on_delete=models.CASCADE)
    NomLigne = models.ForeignKey(Ligne, on_delete=models.CASCADE)
    Date = models.DateTimeField()
    Heure = models.CharField(max_length=15)

    class Meta:
        unique_together = ('IdEmploye', 'Plaque', 'NomLigne', 'Date')
        app_label = 'admin'

class Travaille(models.Model):
    IdEmploye = models.ForeignKey(Employe, on_delete=models.CASCADE)
    IdBranche = models.ForeignKey(Branche, on_delete=models.CASCADE)
    IdService = models.ForeignKey(Service, on_delete=models.CASCADE)
    Date = models.DateTimeField()
    Annee = models.IntegerField()

    class Meta:
        unique_together = ('IdEmploye', 'IdBranche', 'IdService', 'Date')
        app_label = 'admin'