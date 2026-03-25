
from utilisateur.models import UtilisateurModel
from django.shortcuts import get_object_or_404, render
from django.views import View

from produit.models import ProduitModel
from commande.models import CommandeModel, DevisModel


class ConnexionView(View):

    http_method_names = ["get", "post"]
    def get(self,request):
        pass
    
    def post(self,request):
        pass

def ConnexionSuiteUtils(request):
    pass

class ConnexionMotpasseView(View):
    http_method_names = ["get", "post"]
    def get(self,request):
        pass
    
    def post(self,request):
        pass
    
class InscriptionView(View):
    http_method_names = ["get", "post"]
    def get(self,request):
        pass
    
    def post(self,request):
        pass


class MotpasseView(View):
    http_method_names = ["get", "post"]
    def get(self,request):
        pass
    
    def post(self,request):
        pass
       
def DeconnexionGet(request):
    pass

def CompteGet(request):
    ui = get_object_or_404()
    dev1 = DevisModel.obj.filter()
    com1 = CommandeModel.obj.filter()
    response = render(request, 'a2-compte.html' , context={'ui':ui,'dev1':dev1, 'com1':com1}, content_type='text/html')
    return response

def CreateurGet(request,utilisateur_createur_slug:str, utilisateur_id:int):
        ui = get_object_or_404(UtilisateurModel, utilisateur_createur_slug=utilisateur_createur_slug, utilisateur_id=utilisateur_id)
        pr1 = ProduitModel.obj.filter(produit_createur=ui.utilisateur_createur_titre)
        response = render(request, 'a1-createur.html' , context={'ui':ui,'pr1':pr1}, content_type='text/html')
   
        return response

def CreateurListeGet(request):
        cr1 = UtilisateurModel.obj.filter(utilisateur_groupe='createur', utilisateur_createur_noindex=0)
        response = render(request, 'a1-createur-liste.html' , context={'cr1':cr1}, content_type='text/html')
        return response
