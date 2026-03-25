from django.db import models
from imagekit.models import ProcessedImageField


class ProduitManager(models.Manager):
    pass

class ProduitModel(models.Model):
    produit_id = models.AutoField(primary_key=True)
    produit_categorie = models.CharField(null=True, blank=True,max_length=150)
    produit_langue = models.CharField(null=True, blank=True,max_length=150)
    produit_titre = models.CharField(max_length=60)
    produit_description = models.TextField(null=True, blank=True,max_length=255)
  
    produit_prix_ht = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    produit_prix_ttc = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    produit_prix = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
   
    produit_devise = models.CharField(blank=True, max_length=20, default="euros")
    produit_stock = models.IntegerField(null=True, blank=True, default="1")
    produit_slug = models.SlugField(null=False, unique=True)
    produit_url = models.CharField(null=True, blank=True, max_length=250, unique=True)
    
    produit_materiaux = models.CharField(null=True, blank=True,max_length=150)
    produit_image1_min = ProcessedImageField(blank=True, null=True, upload_to='',
                                 processors=[], format='JPEG')
    
    produit_taille1 = models.CharField(blank=True,max_length=10)
    produit_taille2 = models.CharField(blank=True,max_length=10)

    produit_couleur1 = models.CharField(blank=True,max_length=20)
    produit_couleur2 = models.CharField(blank=True,max_length=20)

    produit_question1 = models.CharField(blank=True,max_length=200)
    produit_question11 = models.TextField(null=True, blank=True,max_length=1255)


   
    obj = ProduitManager()
    def __str__(self):
        return self.produit_titre

    class Meta:
        indexes = [models.Index(fields=["produit_id"], )]
        verbose_name = 'produit'



class CategorieManager(models.Manager):
    pass

class CategorieModel(models.Model):
    categorie = models.CharField(null=True,max_length=150)
    categorie_titre = models.CharField(max_length=50)
    categorie_description = models.TextField(max_length=255)
    categorie_slug = models.SlugField(null=False, unique=True)
    categorie_url = models.CharField(null=True, blank=True, max_length=250, unique=True)
    categorie_date = models.DateField(null=True, auto_now_add=True)
   
    categorie_question1 = models.CharField(blank=True,max_length=200)
    categorie_question11 = models.TextField(null=True, blank=True,max_length=1255)

    obj = CategorieManager()
    def __str__(self):
        return self.categorie_titre

    class Meta:
        indexes = [models.Index(fields=["categorie_id"], )]
        verbose_name = 'Categorie'
