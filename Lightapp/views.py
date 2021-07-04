from django.http import HttpResponse, Http404, JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.utils import timezone
from .motdepass import *
from datetime import datetime as dt

# Create your views here.
#############################################################################
def connexion(request):
    error = False
    if request.POST:
        error = False
        print(request.POST)
        if request.POST.get('valider') == 'valider':
            print(request.POST)
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user:  # Si l'objet renvoyé n'est pas None
                if user.is_active:
                    login(request, user)  # nous connectons l'utilisateur
                    return redirect(reverse(index))
                else:
                    error = True
            else: # sinon une erreur sera affichée
                error = True
    else:
        print("Connexion RAS")

    return render(request, 'connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

#############################################################################
@login_required(login_url='') #if not logged in redirect to /
def index(request):
    return render(request, 'index.html', locals())

#############################################################################
@login_required(login_url='') #if not logged in redirect to /
def patient_liste_entrees(request):
    patients = Patients.objects.filter(archive=False)
    return render(request, 'entrees/patient/patient-liste-entrees.html', locals())

@login_required(login_url='') #if not logged in redirect to /
def patient_creer_entrees(request):
    if request.POST:
        error = False
        if request.POST['valider'] == 'valider':

            patient = Patients()
            patient.codepatient = code()
            nompatient = request.POST.get('nompatient')
            patient.nompatient = nompatient.upper()
            prenompatient = request.POST.get('prenompatient')
            patient.prenompatient = prenompatient.capitalize()
            patient.sexepatient = request.POST.get('sexepatient')
            patient.datenaissancepatient = dt.strptime(request.POST.get('datenaissancepatient'), "%d/%m/%Y").date()
            patient.payspatient = request.POST.get('payspatient')
            patient.cnipatient = request.POST.get('cnipatient')
            patient.attestationepatient = request.POST.get('attestationepatient')
            patient.situationmatrimonialepatient = request.POST.get('situationmatrimonialepatient')
            patient.professionpatient = request.POST.get('professionpatient')
            patient.domicileepatient = request.POST.get('domicileepatient')
            patient.telephonepatient = request.POST.get('telephonepatient')
            patient.emailpatient = request.POST.get('emailpatient')
            patient.npperepatient = request.POST.get('npperepatient')
            patient.npmerepatient = request.POST.get('npmerepatientephone')
            patient.telephoneurgencepatient = request.POST.get('telephoneurgencepatient')

            patient.save()
            return redirect('/patient-liste-entrees')
        else:

            return redirect('/patient-liste-entrees')
            
    else:
        form =  PatientForm()
    return render(request, 'entrees/patient/patient-creer-entrees.html', locals())

@login_required(login_url='') #if not logged in redirect to /
def patient_delete_entrees(request, id):
    patients = Patients.objects.get(id = id)
    patients.archive = True
    patients.save()
    return redirect('/patient-liste-entrees')

@login_required(login_url='') #if not logged in redirect to /
def patient_voir_entrees(request, id):
    patients = Patients.objects.get(id = id)
    return render(request, 'entrees/patient/patient-voir-entrees.html', locals())

@login_required(login_url='') #if not logged in redirect to /
def paiement_liste_entrees(request):
    paiements = Paiements.objects.filter(archive=False)
    return render(request, 'entrees/paiement/paiement-liste-entrees.html', locals())

@login_required(login_url='') #if not logged in redirect to /
def paiement_creer_entrees(request):
    patients = Patients.objects.filter(archive=False)
    dates = timezone.now()
    heure = timezone.now()
    if request.POST:
        error = False
        if request.POST['valider'] == 'valider':

            paiement = Paiements()
            paiement.datepaiement = dt.strptime(request.POST.get('datepaiement'), "%d/%m/%Y").date()
            paiement.heurepaiement = request.POST.get('heurepaiement')
            paiement.totalpaiement = int(request.POST.get('totalpaiement'))
            praticien = request.POST.get('praticien')
            paiement.praticien = praticien.upper()
            servicepaiement = request.POST.get('servicepaiement')
            paiement.servicepaiement = servicepaiement.upper()
            paiement.actespaiement = request.POST.get('actespaiement')
            paiement.patient = Patients.objects.get(id = request.POST.get('patient'))
            paiement.save()

            return redirect('/paiement-liste-entrees')
        else:

            return redirect('/paiement-liste-entrees')
    else:
        form =  PaiementForm()
    return render(request, 'entrees/paiement/paiement-creer-entrees.html', locals())

@login_required(login_url='') #if not logged in redirect to /
def paiement_delete_entrees(request, id):
    paiements = Paiements.objects.get(id = id)
    paiements.archive = True
    paiements.save()
    return redirect('/paiement-liste-entrees')

@login_required(login_url='') #if not logged in redirect to /
def paiement_voir_entrees(request, id):
    paiements = Paiements.objects.get(id = id)
    return render(request, 'entrees/paiement/paiement-voir-entrees.html', locals())


@login_required(login_url='') #if not logged in redirect to /
def rdv_liste_entrees(request):
    rdvs = Rdv.objects.filter(archive=False)
    return render(request, 'entrees/rdv/rdv-liste-entrees.html', locals())

@login_required(login_url='') #if not logged in redirect to /
def rdv_creer_entrees(request):
    patients = Patients.objects.filter(archive=False)
    dates = timezone.now()
    heure = timezone.now()
    if request.POST:
        error = False
        if request.POST['valider'] == 'valider':
            
            rdv = Rdv()
            rdv.dateprevu = dt.strptime(request.POST.get('dateprevu'), "%d/%m/%Y").date()
            rdv.heuredebut = request.POST.get('heuredebut')
            rdv.duree = int(request.POST.get('duree'))
            rdv.praticien = request.POST.get('praticien')
            rdv.servicerdv = request.POST.get('servicerdv')
            praticien = request.POST.get('praticien')
            rdv.praticien = praticien.upper()
            servicerdv = request.POST.get('servicerdv')
            rdv.servicerdv = servicerdv.upper()
            rdv.actesrdv = request.POST.get('actesrdv')
            rdv.prioriterdv = request.POST.get('prioriterdv')
            rdv.typerdv = request.POST.get('typerdv')
            rdv.commentaire = request.POST.get('commentaire')
            rdv.patient = Patients.objects.get(id = request.POST.get('patient'))
            rdv.save()

            return redirect('/rdv-liste-entrees')
        else:

            return redirect('/rdv-liste-entrees')
    else:
        form =  RvdForm()
    return render(request, 'entrees/rdv/rdv-creer-entrees.html', locals())

@login_required(login_url='') #if not logged in redirect to /
def rdv_delete_entrees(request, id):
    rdvs = Rdv.objects.get(id = id)
    rdvs.archive = True
    rdvs.save()
    return redirect('/rdv-liste-entrees')

@login_required(login_url='') #if not logged in redirect to /
def rdv_voir_entrees(request, id):
    rdvs = Rdv.objects.get(id = id)
    return render(request, 'entrees/rdv/rdv-voir-entrees.html', locals())

#############################################################################
@login_required(login_url='') #if not logged in redirect to /
def paiement_liste_caisse(request):
    paiements = Paiements.objects.filter(archive=False)
    return render(request, 'caisse/paiement/paiement-liste-caisse.html', locals())

@login_required(login_url='') #if not logged in redirect to /
def recu_liste_caisse(request):
    return render(request, 'caisse/recu/recu-liste-caisse.html', locals())

#############################################################################
@login_required(login_url='') #if not logged in redirect to /
def liste_patient_attente_infirmerie(request):
    return render(request, 'infirmerie/attente/liste-patient-attente-infirmerie.html', locals())

@login_required(login_url='') #if not logged in redirect to /
def liste_patient_recu_infirmerie(request):
    return render(request, 'infirmerie/recu/liste-patient-recu-infirmerie.html', locals())
#############################################################################