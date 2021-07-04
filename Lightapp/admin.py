from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Admin LightApp')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Administration LightApp')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = MyAdminSite()


class AdminPatient(admin.ModelAdmin):
    list_display = ('codepatient','nompatient','prenompatient','sexepatient', 'datenaissancepatient','payspatient','cnipatient',
                    'attestationepatient','situationmatrimonialepatient','domicileepatient','telephonepatient','telephoneurgencepatient','emailpatient',
                    'npperepatient','npmerepatient','archive')
    
    search_fields = ('nompatient', 'prenompatient','datenaissancepatient',  'Num_carte_consulaire',
                     'cnipatient', 'attestationepatient','code_patient','situationmatrimonialepatient','domicileepatient','telephonepatient','telephoneurgencepatient','emailpatient',
                    'npperepatient','npmerepatient')
    
    list_filter = ('nompatient', 'sexepatient', 'situationmatrimonialepatient','archive','payspatient','domicileepatient')

class AdminPaiement(admin.ModelAdmin):
    list_display = ('patient','praticien','datepaiement','heurepaiement', 'servicepaiement','actespaiement',
                    'totalpaiement','Statut','caisse')
    
    search_fields = ('patient','praticien','datepaiement','heurepaiement', 'servicepaiement','actespaiement',
                    'totalpaiement','caisse','Statut','caisse')
    
    list_filter = ('Statut','praticien','archive',)

class AdminRdv(admin.ModelAdmin):
    list_display = ('patient','praticien','dateprevu','heuredebut', 'servicerdv','duree','actesrdv',
                    'prioriterdv','typerdv','commentaire','statut','archive')
    
    search_fields = ('patient','praticien','dateprevu','heuredebut', 'servicerdv','duree','actesrdv',
                    'prioriterdv','typerdv','commentaire','statut')
    
    list_filter = ('statut','praticien','archive',)

admin.site.register(Patients, AdminPatient)
admin.site.register(Paiements, AdminPaiement)
admin.site.register(Rdv, AdminRdv)