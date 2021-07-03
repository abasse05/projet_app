from django.shortcuts import render

# Create your views here.
#############################################################################
def index(request):
    return render(request, 'index.html', locals())

#############################################################################

def patient_liste_entrees(request):
    return render(request, 'entrees/patient/patient-liste-entrees.html', locals())

def paiement_liste_entrees(request):
    return render(request, 'entrees/paiement/paiement-liste-entrees.html', locals())

def rdv_liste_entrees(request):
    return render(request, 'entrees/rdv/rdv-liste-entrees.html', locals())

#############################################################################

def paiement_liste_caisse(request):
    return render(request, 'caisse/paiement/paiement-liste-caisse.html', locals())

def recu_liste_caisse(request):
    return render(request, 'caisse/recu/recu-liste-caisse.html', locals())

#############################################################################

def liste_patient_attente_infirmerie(request):
    return render(request, 'infirmerie/attente/liste-patient-attente-infirmerie.html', locals())

def liste_patient_recu_infirmerie(request):
    return render(request, 'infirmerie/recu/liste-patient-recu-infirmerie.html', locals())
#############################################################################