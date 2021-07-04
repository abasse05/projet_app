from django.db import models
from django.utils import timezone
from .motdepass import *

# Create your models here.

class Patients(models.Model):
    CHOICES = (
        ('Masculin', 'Masculin'),
        ('Feminin','Feminin'),
    )
    COUNTRIES = (
        ('Afrique du sud','Afrique du sud'),
        ('Bénin','Bénin'),
        ('Côte d\'ivoire', 'Côte d\'ivoire'),
        ('Burkina Faso','Burkina Faso'),
        ('France','France'),
        ('Ghana','Ghana'),
        ('Guinée','Guinée'),
        ('Mali','Mali'),
        ('Nigeria','Nigeria'),
        ('Niger','Niger'),
        ('Togo','Togo'),
    )
    SITUATION = (
        ('Marié(e)','Marié(e)'),
        ('Celibataire', 'Celibataire'),
        ('Divorcé(e)','Divorcé(e)'),
        ('Veuf(ve)','Veuf(ve)'),
        ('Autre','Autre'),
    )
    
    codepatient = models.CharField(max_length=255, default=code(),verbose_name='Code')
    #photo = models.ImageField(null=True, blank=True,upload_to="photos_patient/")
    nompatient = models.CharField(max_length=255,verbose_name='Nom patient')
    prenompatient = models.CharField(max_length=255,verbose_name='Prenom patient')
    sexepatient = models.CharField(max_length=10, choices=CHOICES, default='Masculin', verbose_name='Sexe patient')
    datenaissancepatient = models.DateField(default=timezone.now, verbose_name='Date de naissance patient')
    payspatient = models.CharField(max_length=255, choices=COUNTRIES, verbose_name='Pays patient')
    cnipatient = models.CharField(null=True, blank=True, max_length=14, verbose_name='Numéro CNI patient')
    attestationepatient = models.CharField(null=True, blank=True, max_length=14, verbose_name='Numéro Attestation patient')
    situationmatrimonialepatient = models.CharField(null=True, blank=True, max_length=255, choices=SITUATION, verbose_name='Situation matrimoniale patient')
    professionpatient = models.CharField(null=True, blank=True, max_length=14, verbose_name='Profession patient')
    domicileepatient = models.CharField(null=True, blank=True, max_length=255, verbose_name='Domicile patient')
    telephonepatient = models.CharField(blank=True, verbose_name='Téléphone patient', max_length = 100, null=True)
    emailpatient = models.EmailField(blank=True, verbose_name='Email patient', max_length = 100, null=True)
    npperepatient = models.CharField(blank=True, null=True, max_length = 500, verbose_name='Nom et prenoms père patient')
    npmerepatient = models.CharField(blank=True, null=True, verbose_name='TNom et prenoms mère patient', max_length = 500)
    telephoneurgencepatient = models.CharField(max_length=255,verbose_name='Numero urgence patient', blank=True, null=True)
    archive = models.BooleanField(verbose_name="Archiver le patient", default=0)

    class Meta:
        ordering = ('nompatient','prenompatient',) #ranger par ordre decroissant
    
    def __str__(self):
        return "{0} {1}".format(self.nompatient, self.prenompatient)        #return le titre de chaque objet
    
    def get_patient(self):
        return "{0} {1}".format(self.nompatient, self.prenompatient)
    
class Paiements(models.Model):
    CHOIX = (
        ('Ouverte', 'Ouverte'),
        ('Payée', 'Payée'),
        ('Annulée', 'Annulée')
    )
    
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, related_name='Paiement')
    datepaiement = models.DateField(default=timezone.now, verbose_name='Date paiement')
    heurepaiement = models.TimeField(default=timezone.now, verbose_name='Date paiement')
    totalpaiement = models.IntegerField(default=0, verbose_name='Total paiement')
    praticien =  models.CharField(max_length=255, null=True, blank=True, verbose_name='Praticien')
    archive = models.BooleanField(default=False)
    Statut = models.CharField(max_length=255, choices=CHOIX, default='Ouverte', verbose_name='Statut')
    caisse = models.BooleanField(default=False)
    servicepaiement = models.CharField(max_length=255, verbose_name='Service', blank=True, null=True)
    actespaiement = models.TextField(verbose_name='Actes', blank=True, null=True)

    class Meta:
        ordering = ('datepaiement','heurepaiement',) #ranger par ordre decroissant
    
    def __str__(self):
        return "{0} {1}".format(self.patient, self.servicepaiement) 

class Rdv(models.Model):
    PRIORITES = (
        ('Normal','Normal'),
        ('Urgences','Urgences')
    )
    RDV = (
        ('Normal','Normal'),
        ('Contrôle','Contrôle')
    )
    STAT = (
        ('A effectué', 'A effectué'),
        ('Effectué', 'Effectué')
    )
    
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, related_name='rdv')
    praticien =  models.CharField(max_length=255, null=True, blank=True, verbose_name='Praticien')
    dateprevu = models.DateField(default=timezone.now, verbose_name='Date RDV')
    heuredebut = models.TimeField(null=True, blank=True, verbose_name='Heure debut')
    servicerdv = models.CharField(max_length=255, verbose_name='Service', blank=True, null=True)
    duree = models.IntegerField(default=0, null=True, blank=True, verbose_name='Duree')
    actesrdv = models.TextField(verbose_name='Service', blank=True, null=True)
    prioriterdv = models.CharField(max_length=255, choices=PRIORITES, default='Normal', verbose_name='Priorite')
    typerdv = models.CharField(max_length=255, choices=RDV, default='Normal', verbose_name='Type RDV')
    statut = models.CharField(max_length=255, choices=STAT, default='A effectué', verbose_name='Statut')
    commentaire = models.TextField(verbose_name='Commentaires', blank=True, null=True)
    archive = models.BooleanField(default=False)

    class Meta:
        ordering = ('dateprevu','heuredebut',) #ranger par ordre decroissant
    
    def __str__(self):
        return "{0} {1}".format(self.patient, self.praticien) 