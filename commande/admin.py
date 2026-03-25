from django.contrib import admin
from commande.models import CommandeModel, FicheModel, PanierModel, DevisModel, LivraisonModel

admin.site.register([CommandeModel, FicheModel, PanierModel, DevisModel, LivraisonModel])