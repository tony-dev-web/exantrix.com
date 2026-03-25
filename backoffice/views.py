from produit.models import ProduitModel, CategorieModel
from django.shortcuts import render
from itertools import chain

def SitemapGet(request):
    up1 = list(chain(ProduitModel.obj.filter(), CategorieModel.obj.filter()))
    return render(request, "sitemap-web.xml",{'up1':up1}, content_type='text/xml')

def RobotGet(request):
    return render(request, "robots.txt", content_type='text/plain')

