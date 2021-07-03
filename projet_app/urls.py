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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),

    #############################################################################
    path('patient-liste-entrees/', views.patient_liste_entrees, name='patient-liste-entrees'),
    path('paiement-liste-entrees/', views.paiement_liste_entrees, name='paiement-liste-entrees'),
    path('rdv-liste-entrees/', views.rdv_liste_entrees, name='rdv-liste-entrees'),

    #############################################################################
    path('paiement-liste-caisse/', views.paiement_liste_caisse, name='paiement-liste-caisse'),
    path('recu-liste-caisse/', views.recu_liste_caisse, name='recu-liste-caisse'),
    
    #############################################################################
    path('liste-patient-attente-infirmerie/', views.liste_patient_attente_infirmerie, name='liste-patient-attente-infirmerie'),
    path('liste-patient-recu-infirmerie/', views.liste_patient_recu_infirmerie, name='liste-patient-recu-infirmerie'),
]
