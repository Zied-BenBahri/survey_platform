from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.

#  table Gouvernorat
class Gouvernorat(models.Model):
    libelle = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.libelle

#  table Delegation
class Delegation(models.Model):
    libelle = models.CharField(max_length=100, unique=True)
    gouvernorat = models.ForeignKey(Gouvernorat, on_delete=models.CASCADE, related_name='delegations')

    def __str__(self):
        return self.libelle

#  table Imada
class Localite(models.Model):
    libelle = models.CharField(max_length=100, unique=True)
    delegation = models.ForeignKey(Delegation, on_delete=models.CASCADE, related_name='localites')

    def __str__(self):
        return self.libelle

#  table User
class User(AbstractUser):
    gouvernorat = models.ForeignKey(Gouvernorat, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.username
"""
class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gouvernorat = models.ForeignKey(Gouvernorat, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.user.username
"""
#  table Enquete
class Enquete(models.Model):

    statutResidence_CHOICES = (
        ('urbain', 'Urbain'),
        ('rural', 'Rural'),
    )
    nbPersFoyer_CHOICES = (
        ('1-2', '1-2'),
        ('3-4', '3-4'),
        ('5-6', '5-6'),
        ('7 et plus', '7 et plus'),
    )
    revMensuel_CHOICES = (
        ('moins de 500 TND', 'Moins de 500 TND'),
        ('500 - 1000 TND', '500 - 1000 TND'),
        ('1000 - 1500 TND', '1000 - 1500 TND'),
        ('plus de 1500 TND', 'Plus de 1500 TND'),
    )
    NivEduc_CHOICES = (
        ('aucun', 'Aucun'),
        ('primaire', 'Primaire'),
        ('secondaire', 'Secondaire'),
        ('superieur', 'Supérieur'),
    )
    typeBiomasse_CHOICES = (
        ('bois de chauffage','Bois de chauffage'),
        ('residus agricoles','Résidus agricoles'),
        ('dechets vegetaux','Déchets végétaux'),
        ('charbon de bois','Charbon de bois'),
        ('autre','Autre (précisez)')
    )
    usageBiomasse_CHOICES = (
        ('cuisson des aliments', 'Cuisson des aliments'),
        ('chauffage', 'Chauffage'),
        ('cuisson de pain', 'Cuisson de pain'),
        ('production d eau chaude', "Production d'eau chaude"),
        ('autre','Autre (précisez)')
    )
    sourceApprov_CHOICES = (
        ('forets locales', 'Forêts locales'),
        ('exploitations agricoles', 'Exploitations agricoles'),
        ('marches locaux', 'Marchés locaux'),
        ('collecte de dechets vegetaux', "Collecte de déchets végétaux"),
        ('autre','Autre (précisez)')
    )
    raisonUsage_CHOICES = (
        ('cout inferieur', "Coût inférieur par rapport à d'autres sources d'énergie"),
        ('disponibilite locale', 'Disponibilité locale'),
        ('tradition', 'Tradition'),
        ('fiabilite', 'Fabilité'),
        ('autre','Autre (précisez)')
    )
    changerEnergie_CHOICES = (
        ('oui', 'Oui'),
        ('non', 'Non')
    )
    sourceAlter_CHOICES = (
        ('gaz naturel', 'Gaz naturel'),
        ('electricite', 'Électricité'),
        ('energies renouvelables', 'Énergies renouvelables (solaire, …)'),
        ('autre','Autre')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE,default="admin", related_name='enquetes')
    #delegation = models.ForeignKey(Delegation, on_delete=models.CASCADE, related_name='enquetes')
    localite = models.ForeignKey(Localite, on_delete=models.SET_NULL,null=True, related_name='enquetes')
    
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)   
     
    statutResidence = models.CharField(max_length=20, null=False, blank=False,choices=statutResidence_CHOICES, verbose_name="Statut de Résidence")
    nbPersFoyer = models.CharField(max_length=20, null=False, blank=False,choices=nbPersFoyer_CHOICES,verbose_name="Nombre de personnes dans le foyer :")
    revMensuel = models.CharField(max_length=30, null=False, blank=False,choices=revMensuel_CHOICES,verbose_name="Quel est votre niveau de revenu mensuel moyen ?")
    NivEduc = models.CharField(max_length=30, null=False, blank=False,choices=NivEduc_CHOICES,verbose_name="Niveau d'éducation du chef de foyer :")
    
    typeBiomasse = models.CharField(max_length=200, null=True, blank=False,verbose_name=" Quels types de biomasse utilisez-vous pour vos besoins énergétiques ? ")
    typeBiomasse_autre = models.CharField(max_length=300, null=True, blank=True, verbose_name="Autre type de biomasse (précisez)")
    
    usageBiomasse = models.CharField(max_length=200, null=True, blank=False,verbose_name="Pour quels usages principaux utilisez-vous la biomasse ? ")
    Usagebiomasse_autre = models.CharField(max_length=300, null=True, blank=True, verbose_name="Autre usage de biomasse (précisez)")


    QteBoisChauffage = models.IntegerField(
        default=0,
        verbose_name="Bois de chauffage en kg/mois "
    )
    QteResiduAgric = models.IntegerField(
        default=0,
        verbose_name="Résidus agricoles en kg/mois "
    )
    QteDechetsVeget = models.IntegerField(
        default=0,
        verbose_name="Déchets végétaux en kg/mois "
    )
    QteCharbonBois = models.IntegerField(
        default=0,
        verbose_name="Charbon de bois en kg/mois "
    )
    sourceApprov = models.CharField(max_length=200, null=False, blank=False,verbose_name="Quelle est votre principale source d'approvisionnement en biomasse ?")
    sourceApprov_autre = models.CharField(max_length=200, null=True, blank=True, verbose_name="Autre source d'approvisionnement (précisez)")


    raisonUsage = models.CharField(max_length=300, null=False, blank=False,verbose_name=" Pourquoi utilisez-vous principalement la biomasse ?")
    raisonUsage_autre = models.CharField(max_length=300, null=True, blank=True, verbose_name="Autre raison d'utilisation (précisez)")

    changerEnergie = models.CharField(max_length=10, null=False, blank=False,choices=changerEnergie_CHOICES,verbose_name="Seriez-vous disposé à passer à une autre source d'énergie si elle était disponible et abordable ?")
    changerEnergie_pourquoi = models.CharField(max_length=300, null=True, blank=True, verbose_name="Si non, pourquoi?")

    
    sourceAlter = models.CharField(max_length=150, null=False, blank=False,verbose_name="Quelles autres sources d'énergie utilisez-vous ou envisagez-vous d'utiliser ? ")
    sourceAlter_autre = models.CharField(max_length=300, null=True, blank=True, verbose_name="Autre source d'énergie (précisez)")



    
    def clean(self):
        if self.QteBoisChauffage < 0:
            raise ValidationError('La quantité de bois de chauffage doit être positive.')
        if self.QteResiduAgric < 0:
            raise ValidationError('La quantité de résidus agricoles doit être positive.')
        if self.QteDechetsVeget < 0:
            raise ValidationError('La quantité de déchets végétaux doit être positive.')
        if self.QteCharbonBois < 0:
            raise ValidationError('La quantité de charbon de bois doit être positive.')
        if self.localite.delegation.gouvernorat != self.agent.gouvernorat:
            raise ValidationError("La localité doit appartenir à une délégation du gouvernorat de l'agent.")

    def __str__(self):
        return f'Enquete {self.id}'

    def save(self, *args, **kwargs):
        self.clean()  # This calls the clean method to perform validation
        super().save(*args, **kwargs)
