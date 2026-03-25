from django.contrib import admin
from produit.models import ProduitModel, CategorieModel

admin.site.register([ProduitModel, CategorieModel])