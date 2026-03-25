
from django.urls import path
from backoffice.views import RobotGet
from page.views import IndexGet, MentionGet, DtfGet, DtfPoseGet, PlotterGet, DecoupeGet, FermeGet, ScannerGet, DiyGet, LogicielGet, CgvGet, EvenementListeGet, EvenementGet, ParametreListeGet, Parametre3dGet, ParametreDtfGet
from commande.views import  DevisView
from utilisateur.views import CreateurListeGet, CreateurGet
from produit.views import CategorieListeGet, CategorieGet, ProduitView

urlpatterns = [
    path('', IndexGet),
    path('robots.txt', RobotGet),
    path('mentions-legales', MentionGet),
    path('cgv', CgvGet),
    path('fichier-devis-impression-3d/', DevisView.as_view()),
    path('ferme-service-imprimante-3d', FermeGet),
    path('decoupe-gravure-bois-metal', DecoupeGet),
    path('plotter-decoupe-vinyle-rouleau', PlotterGet),
    path('dtf-imprimante-transfert-textile', DtfGet),
    path('dtf-imprimante-transfert-textile/transfert-dtf-pose-pressage', DtfPoseGet),
    path('scanner-3d-numerisation-objet', ScannerGet),
    path('diy-faites-le-vous-meme', DiyGet),
    path('logiciel-3d-modelisation-cao-developpement', LogicielGet),
    path('evenements/', EvenementListeGet),
    path('evenements/<str:evenement_slug>-<int:evenement_id>/', EvenementGet),
    path('categorie/', CategorieListeGet),
    path('categorie/<str:categorie_slug>-<int:categorie_id>/', CategorieGet, name="categorie_url"),
    path('<str:produit_slug>-<int:produit_id>/', ProduitView.as_view(), name="produit_url"),
    path('createurs/<str:utilisateur_createur_slug>-<int:utilisateur_id>/', CreateurGet, name="createur_url"),
    path('createurs/', CreateurListeGet),
    path('parametres/fichier-impression-3d-3mf-stl', Parametre3dGet),
    path('parametres/fichier-dtf-impression-cmyk-w-300-dpi', ParametreDtfGet),
    path('parametres/', ParametreListeGet)
]