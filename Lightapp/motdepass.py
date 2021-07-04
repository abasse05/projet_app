import datetime

#code du patient à la création 
def code(): 
    x = datetime.datetime.now()
    mois = str(x.strftime("%H")) + str(x.strftime("%S")) + str(x.strftime("%M")) + str(x.month)
    micro = str(x.strftime("%f"))

    while len(mois) < 8:
        mois = '0' + mois
        
    chars = 'MED-' + str(x.year) + '-' + mois + '-' + micro
    
    return chars

#code du professionnel à la création 
def motdepass_professionnel(): 
    x = datetime.datetime.now()
    mois = str(x.strftime("%H")) + str(x.strftime("%S")) + str(x.strftime("%M")) + str(x.month)
    micro = str(x.strftime("%f"))

    while len(mois) < 8:
        mois = '0' + mois
        
    chars = 'PROF-' + str(x.year) + '-' + mois + '-' + micro
    
    return chars

#
#code du constante à la création 
def motdepass_constante(): 
    x = datetime.datetime.now()
    mois = str(x.strftime("%H")) + str(x.strftime("%S")) + str(x.strftime("%M")) + str(x.month)
    micro = str(x.strftime("%f"))

    while len(mois) < 8:
        mois = '0' + mois
        
    chars = 'CONST-' + str(x.year) + '-' + mois + '-' + micro
    
    return chars


def fiche_payement(): 
    x = datetime.datetime.now()
    mois = str(x.strftime("%H")) + str(x.strftime("%S")) + str(x.strftime("%M")) + str(x.month)
    micro = str(x.strftime("%f"))

    while len(mois) < 7:
        mois = '0' + mois
        
    chars = 'PAY-' + str(x.year) + '-' + mois + '-' + micro
    
    return chars

def ref_recus(): 
    x = datetime.datetime.now()
    mois = str(x.strftime("%H")) + str(x.strftime("%S")) + str(x.strftime("%M")) + str(x.month)
    micro = str(x.strftime("%f"))

    while len(mois) < 6:
        mois = '0' + mois
        
    chars = 'REC-' + str(x.year) + '-' + mois + '-' + micro
    
    return chars

def ref_rendezvous(): 
    x = datetime.datetime.now()
    mois = str(x.strftime("%H")) + str(x.strftime("%S")) + str(x.strftime("%M")) + str(x.month)
    micro = str(x.strftime("%f"))

    while len(mois) < 6:
        mois = '0' + mois
        
    chars = 'RDV-' + str(x.year) + '-' + mois + '-' + micro
    
    return chars