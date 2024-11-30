# insert_data.py
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'survey.settings')
django.setup()

from enquete.models import Gouvernorat, Delegation, Localite

# List of governorates with their delegations and localities
tunisia_data = {
    "Tunis": {
        "Bab Bhar": ["Localite 1", "Localite 2"],
        "Bab Souika": ["Localite 3", "Localite 4"],
        # Add other delegations and their localities
    },

    #"Ariana": {
     #   "Ariana Ville": ["Localite 1", "Localite 2"],
      #  "Ettadhamen": ["Localite 3", "Localite 4"],
        # Add other delegations and their localities
    #},
    # Add other governorates, their delegations and localities
}

# Insert data into the database
for gov_name, delegations in tunisia_data.items():
    if not(Gouvernorat.objects.get(libelle=gov_name)):
       gouvernorat = Gouvernorat.objects.create(libelle=gov_name)
    else :
        gouvernorat =Gouvernorat.objects.get(libelle=gov_name)
    for deleg_name, localites in delegations.items():

        delegation = Delegation.objects.create(libelle=deleg_name, gouvernorat=gouvernorat)
        for localite_name in localites:
            Localite.objects.create(libelle=localite_name, delegation=delegation)

print("Data inserted successfully")
