"""projet_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Lightapp import views
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.connexion, name='connexion'),
    path('index/', views.index, name='index'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),

    #############################################################################
    path('patient-liste-entrees/', views.patient_liste_entrees, name='patient-liste-entrees'),
    path('patient-creer-entrees/', views.patient_creer_entrees, name='patient-creer-entrees'),
    path('patient-voir-entrees/<int:id>/', views.patient_voir_entrees, name='patient-voir-entrees'),
    path('patient-delete-entrees/<int:id>/', views.patient_delete_entrees, name='patient-delete-entrees'),
    
    path('paiement-liste-entrees/', views.paiement_liste_entrees, name='paiement-liste-entrees'),
    path('paiement-creer-entrees/', views.paiement_creer_entrees, name='paiement-creer-entrees'),
    path('paiement-voir-entrees/<int:id>/', views.paiement_voir_entrees, name='paiement-voir-entrees'),
    path('paiement-delete-entrees/<int:id>/', views.paiement_delete_entrees, name='paiement-delete-entrees'),

    path('rdv-liste-entrees/', views.rdv_liste_entrees, name='rdv-liste-entrees'),
    path('rdv-creer-entrees/', views.rdv_creer_entrees, name='rdv-creer-entrees'),
    path('rdv-voir-entrees/<int:id>/', views.rdv_voir_entrees, name='rdv-voir-entrees'),
    path('rdv-delete-entrees/<int:id>/', views.rdv_delete_entrees, name='rdv-delete-entrees'),
    #############################################################################
    path('paiement-liste-caisse/', views.paiement_liste_caisse, name='paiement-liste-caisse'),
    path('recu-liste-caisse/', views.recu_liste_caisse, name='recu-liste-caisse'),

    #############################################################################
    path('liste-patient-attente-infirmerie/', views.liste_patient_attente_infirmerie, name='liste-patient-attente-infirmerie'),
    path('liste-patient-recu-infirmerie/', views.liste_patient_recu_infirmerie, name='liste-patient-recu-infirmerie'),
]
