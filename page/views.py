from produit.models import CategorieModel
from django.shortcuts import get_object_or_404, render
from page.models import EvenementModel

def IndexGet(request):
    uc1 = CategorieModel.obj.filter()
    response = render(request, 'a1-index.html' , context={'uc1':uc1}, content_type='text/html')
    return response

def CgvGet(request):
    response = render(request, 'a1-cgv.html', content_type='text/html')
    return response

def MentionGet(request):
    response = render(request, 'a1-mentions.html', content_type='text/html')
    return response

def FermeGet(request):
    response = render(request, 'a1-ferme.html', content_type='text/html')
    return response

def DecoupeGet(request):
    response = render(request, 'a1-decoupe.html', content_type='text/html')
    return response

def PlotterGet(request):
    response = render(request, 'a1-plotter.html', content_type='text/html')

    return response

def DtfGet(request):
    response = render(request, 'a1-dtf.html', content_type='text/html')
   
    return response

def DtfPoseGet(request):
    response = render(request, 'a1-dtf-pose.html', content_type='text/html')
    
    return response

def ScannerGet(request):
    response = render(request, 'a1-scanner.html', content_type='text/html')
    return response

def DiyGet(request):
    response = render(request, 'a1-diy.html', content_type='text/html')
    return response

def LogicielGet(request):
    response = render(request, 'a1-logiciel.html', content_type='text/html')
    return response

def EvenementListeGet(request):
    response = render(request, 'a1-evenement-liste.html', content_type='text/html')
    return response

def EvenementGet(request, evenement_slug:str, evenement_id:int):
    ui = get_object_or_404(EvenementModel,evenement_slug=evenement_slug, evenement_id=evenement_id)
    response = render(request, 'a1-evenement.html' , context={'ui':ui}, content_type='text/html')
    return response


def ParametreListeGet(request):
    response = render(request, 'a1-parametre.html', content_type='text/html')
    return response

def ParametreDtfGet(request):
    response = render(request, 'a1-parametre-dtf.html', content_type='text/html')
    return response

def Parametre3dGet(request):
    response = render(request, 'a1-parametre-3d.html', content_type='text/html')
    return response