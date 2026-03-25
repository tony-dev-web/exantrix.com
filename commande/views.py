#import json
import datetime
import stripe
from django.shortcuts import redirect, render
from django.views import View
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from utilisateur.models import UtilisateurModel
from commande.models import CommandeModel,PanierModel
from django.contrib import messages
from commande.models import FicheModel
from django.db.models import Sum
from commande.models import DevisModel
from page.utils import EmailUtils
from core.utils import PreconnectUtils
from itertools import chain


class CommandeReponseView(View):
    http_method_names = ["get", "post"]
    def get(self,request):
        return render(request, 'a2-commande-reponse.html', content_type='text/html')

    def post(self,request, totalget=0):
    
    
        if request.method != "POST":
                return HttpResponseRedirect('/a2/px1')
        
        pan1 = PanierModel.obj.filter(panier_session=request.key, panier_utilisateur_id=request.user.id)
        #.values_list('panier_id', flat=True)
        
        for ii in pan1:
            PanierModel.obj.get(panier_session=request.session.session_key, panier_utilisateur_id=request.user.id, panier_id=ii.panier_id).update(panier_fichier1=request.POST[f'fichier1-{ii.panier_id}'])
               
        
        
        return







stripe.api_key = 'XXXXXXXXXXXX'

def totalget(request):
    totalget = 0
    if PanierModel.obj.filter(panier_session=request.session.session_key).exists():
        return PanierModel.obj.filter(panier_session=request.session.session_key).aggregate(Sum('panier_prix_ttc_total'))['panier_prix_ttc_total__sum']


    
    return

class CommandeView(View):
    http_method_names = ["get", "post"]
    def get(self,request):
        pan1 = 0
        if PanierModel.obj.filter(panier_session=request.session.session_key).exists():
            pan1 = PanierModel.obj.filter(panier_session=request.session.session_key)
        return  HttpResponse(loader.get_template('a2-commande.html').render({'pan1':pan1,'total':totalget(request)}, request))

    def post(self,request, totalget=0):
        
        ################. A finir
        
        if request.method != "POST":
            return HttpResponseRedirect('/a2/px1')
        
        if not request.user.is_authenticated():
            messages.info(request, 'Vous devez être connecter pour continué')
            return HttpResponseRedirect('/a2/px1')
        
        pan1 = PanierModel.obj.filter(panier_session=request.session.session_key, panier_utilisateur_id=request.user.id).values_list('panier_id', flat=True)
        uti1 = UtilisateurModel.obj.get(utilisateur_id=request.user.id)
        
        if int(totalget(request)) <= 7 :
            #ErreurUtils('paiement-minimum-erreur', 0, request.user.id)
            messages.info(request, 'Vous devez effectuer un paiement minimum de 7 euros')
            return HttpResponseRedirect('/a2/px1')
        
        prix2 = int(totalget(request)) * 100

        com1 = CommandeModel.obj.create(commande_utilisateur_id=request.user.id)
        
        com1.commande_panier_list_id = list(pan1)
        #com1.commande_panier_list_id = list(chain(pan1))
        com1.commande_liv_nom=request.POST['nom']
        com1.commande_liv_prenom=request.POST['prenom']
        com1.commande_liv_email=request.POST['email']
        com1.commande_liv_telephone=request.POST['telephone']
        com1.commande_liv_adresse=request.POST['adresse-liv']
        com1.commande_liv_code_postale=request.POST['code-postale-liv']
        com1.commande_liv_ville=request.POST['ville-liv']
        com1.commande_information=request.POST['information']
        com1.commande_taux_tva = 2.00
        #com1.commande_prix_ht = prix2
        com1.commande_prix_ttc = prix2
        com1.save()
        
        #EmailUtils(request, emailing=paie1.email, messaging=message_email, sujeting=sujet_email ) 

        checkout_session = stripe.checkout.Session.create(
                    
                    )
        return redirect(checkout_session.url)
        
       # return HttpResponseRedirect('/a2/px3')


class DevisView(View):
    http_method_names = ["get", "post"]
    def get(self,request):
        response = render(request, 'a1-devis.html', content_type='text/html')
        response['Link'] = f'<https://exantrix.com/fichier-devis-impression-3d/>;rel="canonical", {PreconnectUtils}'
        #response.headers['Cache-Control'] = 'public, max-age=10800' 
        return response

    
    def post(self, request):
        if request.method != "POST" or not request.POST['email'] or not request.POST['nom']:
            return HttpResponseRedirect('/')
        
        if int(request.POST['calcul']) != 4 :
            messages.info(request, 'Erreur de calcul')
            return HttpResponseRedirect('/fichier-devis-impression-3d/')
        
        dev1 = DevisModel.obj.create(devis_email=request.POST['email'])
        dev1.devis_nom = request.POST['nom']
        dev1.devis_connu = request.POST['connu']
        dev1.devis_information = request.POST['information']
        dev1.devis_date = str(datetime.datetime.now())
        dev1.devis_fichiers = request.POST['fichier1']
        dev1.save()
        
        sujet_email = 'Devis exantrix'
        message_email = 'Demande de contact effectuer avec succès, réponse sous 24 heures'
        EmailUtils(request, emailing=dev1.devis_email, messaging=message_email, sujeting=sujet_email ) 
        #ErreurUtils('contact-formulaire-ok', 1, request.user.id)
        messages.info(request, message_email)
        return HttpResponseRedirect('/fichier-devis-impression-3d/')


def FicheReponseGet(request):
    return render(request, 'a2-fiche-client-reponse.html', content_type='text/html')

class FicheView(View):
    http_method_names = ["get", "post"]
    def get(self,request):
        #lang = lang or 'fr'
        #ui = get_object_or_404(PageModel, page='fret-formulaire')
        response = render(request, 'a2-fiche-client.html', content_type='text/html')
        #response =  HttpResponse(loader.get_template(ui.template).render({'ui':ui,'bodys':LayoutUtils(lang)}, request))
        return response

    def post(self,request):
        fic1 = FicheModel.obj.create(fiche_fichier=request.POST['fichier'], fiche_nom=request.POST['nom'],fiche_prenom=request.POST['prenom'], fiche_email=request.POST['email'], fiche_telephone=request.POST['telephone'], fiche_adresse=request.POST['adresse'], fiche_code_postale=request.POST['code-postale'], fiche_ville=request.POST['ville'], fiche_information=request.POST['information'], fiche_prix=request.POST['prix'], fiche_payer=request.POST['payer'],  fiche_lieu=request.POST['lieu'])
        fic1.save()
        uti1 = UtilisateurModel.obj.create(utilisateur_nom=request.POST['nom'], utilisateur_prenom=request.POST['prenom'], utilisateur_email=request.POST['email'], utilisateur_telephone=request.POST['telephone'], utilisateur_adresse=request.POST['adresse'], utilisateur_code_postale=request.POST['code-postale'], utilisateur_ville=request.POST['ville'], utilisateur_information=request.POST['information'])
        uti1.save()
        return HttpResponseRedirect('/fiche-reponse/')