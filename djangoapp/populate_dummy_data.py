import os
import django
from faker import Faker
from webapp.models import Vehicules, Ligne, Employe, Ticket, Branche, Service, Vend, Conduit, Travaille
from decimal import Decimal  # Import Decimal for phone numbers

# Initialize Django if not already initialized
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapp.settings")
django.setup()


# Create a Faker instance
fake = Faker()

# Custom provider for Arabic names
class ArabicNamesProvider:
    def __init__(self, generator):
        self.generator = generator
        self.first_names = ["Ahmed", "Fatima", "Mohammed", "Amina", "Omar", "Sara", "Ali", "Lina", "Hassan", "Nour", "Khalid", "Layla"]
        self.last_names = ["Abdullah", "Alawi", "Hassan", "Khalid", "Mahmoud", "Nour", "Said", "Ismail", "Othman", "Saleh", "Youssef"]

    def arabic_name(self):
        first_name = self.generator.random_element(self.first_names)
        last_name = self.generator.random_element(self.last_names)

        # Generate a random Nationalite with a maximum length of 20 characters
        nationalite = self.generator.text(max_nb_chars=20)

        # Return a dictionary with the generated values
        return {
            'first_name': first_name,
            'last_name': last_name,
            'nationalite': "Marocain"
        }

# Add the ArabicNamesProvider to Faker
fake.add_provider(ArabicNamesProvider)

# Populate the Vehicules model with dummy data
# for _ in range(10):  # Create 10 dummy Vehicules objects
#     vehicule = Vehicules(
#         Plaque=fake.unique.random_int(min=1000000, max=9999999),
#         Marque=fake.random_element(elements=('Toyota', 'Honda', 'Ford', 'Chevrolet')),
#         Place=fake.random_int(min=1, max=10),
#         Etat=fake.random_element(elements=('Active', 'Inactive', 'Under Maintenance'))
#     )
#     vehicule.save()

# Populate the Ligne model with dummy data


# Populate the Employe model with dummy data
for _ in range(15):  # Create 20 dummy Employe objects
    employe = Employe(
        IdEmploye=fake.unique.random_int(min=10000, max=99999),
        Nom=fake.arabic_name()['first_name'],
        Prenom=fake.arabic_name()['last_name'],
        Nationalite=fake.arabic_name()['nationalite'],  # Use the ArabicNamesProvider
        CarteIdentite=fake.random_int(min=100000, max=999999),
        Phone=Decimal(fake.random_int(min=1000000000, max=9999999999)),  # Generate valid phone numbers
        Etat=fake.random_element(elements=('Active', 'Inactive', 'On Leave'))
    )
    employe.save()


for _ in range(5):  # Create 5 dummy Ligne objects
    ligne = Ligne(
        Nom=fake.unique.job(),
        Prix=fake.random_int(min=10, max=50),
        Heures=fake.random_element(elements=('Morning', 'Afternoon', 'Evening')),
        Interval=fake.random_element(elements=('15 minutes', '30 minutes', '1 hour'))
    )
    ligne.save()
# Populate the Ticket model with dummy data
for _ in range(150):  # Create 15 dummy Ticket objects
    ticket = Ticket(
        NumeroTicket=fake.unique.random_int(min=1000, max=9999),
        NomClient=fake.name()
    )
    ticket.save()

# Populate the Branche model with dummy data
for _ in range(5):  # Create 5 dummy Branche objects
    branche = Branche(
        IdBranche=fake.unique.random_int(min=1000, max=9999),
        Nom=fake.city(),
        Localisation=fake.country(),
        Etat=fake.random_element(elements=('Active', 'Inactive'))
    )
    branche.save()

# Populate the Service model with dummy data
for _ in range(3):  # Create 3 dummy Service objects
    service = Service(
        IdService=fake.unique.random_int(min=100, max=999),
        NomService=fake.random_element(elements=('Sales', 'Support', 'Logistics'))
    )
    service.save()

# Populate the Vend model with dummy data
for _ in range(100):  # Create 30 dummy Vend objects
    vend = Vend(
        NumeroTicket=Ticket.objects.order_by('?').first(),
        NomLigne=Ligne.objects.order_by('?').first(),
        IdEmploye=Employe.objects.order_by('?').first(),
        Heure=fake.time(pattern="%H:%M:%S"),
        DateDepart=fake.date_time_this_decade(before_now=True, after_now=False)
    )
    vend.save()

# Populate the Conduit model with dummy data
for _ in range(50):  # Create 50 dummy Conduit objects
    conduit = Conduit(
        IdEmploye=Employe.objects.order_by('?').first(),
        Plaque=Vehicules.objects.order_by('?').first(),
        NomLigne=Ligne.objects.order_by('?').first(),
        Date=fake.date_time_this_century(),
        Heure=fake.time(pattern="%H:%M:%S")
    )
    conduit.save()


# Populate the Travaille model with dummy data
# for _ in range(40):  # Create 40 dummy Travaille objects
#     travaille = Travaille(
#         IdEmploye=Employe.objects.order_by('?').first(),
#         IdBranche=Branche.objects.order_by('?').first(),
#         IdService=Service.objects.order_by('?').first(),
#         Date=fake.date_time_this_decade(before_now=True, after_now=False),
#         Annee=fake.random_int(min=2000, max=2022)
#     )
#     travaille.save()

print("Dummy data populated successfully!")
