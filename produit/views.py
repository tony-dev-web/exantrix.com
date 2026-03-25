import datetime
from django.shortcuts import get_object_or_404, render
from produit.models import ProduitModel, CategorieModel
from django.views.generic.base import View
from commande.models import PanierModel
from django.http.response import HttpResponseRedirect


class ProduitView(View):
    http_method_names = ["get","post"]
    def get(self,request,produit_slug:str,produit_id:int):
        ui = get_object_or_404(ProduitModel,produit_slug=produit_slug, produit_id=produit_id)
        uc = CategorieModel.obj.get(categorie=ui.produit_categorie)
        pr1 = ProduitModel.obj.filter(produit_prix_ttc='1')

        
        response = render(request, 'a1-produit.html' , context={'pr1':pr1, 'ui':ui, 'uc':uc}, content_type='text/html')
        return response
    
    def post(self, request, produit_slug:str,produit_id:int):
        
        if request.method != "POST":
            return HttpResponseRedirect('/')
        
        ui = get_object_or_404(ProduitModel, produit_slug=produit_slug, produit_id=produit_id)
        pan1 = PanierModel.obj.create(panier_produit_id=produit_id)
        pan1.panier_langue = 'fr'
        pan1.panier_titre = ui.produit_titre
        pan1.panier_url = ui.produit_url
        pan1.panier_date = str(datetime.datetime.now())
        pan1.panier_quantite = int(request.POST['quantite'])
        
        pan1.panier_marque = ui.produit_marque
        pan1.panier_prix_ttc = ui.produit_prix_ttc
        pan1.panier_prix_devise = ui.produit_devise
        pan1.panier_prix_ht = ui.produit_prix_ht
        pan1.panier_prix_ttc_total = ui.produit_prix_ttc * int(request.POST['quantite'])
        pan1.panier_prix_ht_total = ui.produit_prix_ht * int(request.POST['quantite'])
    
        pan1.save()
        
        return HttpResponseRedirect('/a2/px1')


def CategorieGet(request,categorie_slug:str,categorie_id:int):
        ui = get_object_or_404(CategorieModel, categorie_slug=categorie_slug, categorie_id=categorie_id)
        pr1 = ProduitModel.obj.filter(produit_categorie=ui.categorie)
        
        response = render(request, 'a1-categorie.html' , context={'pr1':pr1, 'ui':ui}, content_type='text/html')
        return response
    
def CategorieListeGet(request):
        pr1 = ProduitModel.obj.filter()
        uc1 = CategorieModel.obj.filter()
        response = render(request, 'a1-categorie-liste.html' , context={'pr1':pr1,'uc1':uc1}, content_type='text/html')
        return response

def PanierSupprimeGet(request):
    PanierModel.obj.filter(panier_session=request).delete()
    return HttpResponseRedirect("/a2/px1")

def PanierSupprimeProduitGet(request):
    PanierModel.obj.filter(panier_session=request.id).delete()
    return HttpResponseRedirect("/a2/px1")
        