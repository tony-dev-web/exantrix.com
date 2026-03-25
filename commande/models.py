
from django.db import models
from django.urls import reverse


class CommandeManager(models.Manager):
    pass

class CommandeModel(models.Model):
    commande_id = models.AutoField(primary_key=True)
    commande_session = models.CharField(null=True,max_length=150)
    commande_langue = models.CharField(max_length=150)
    commande_euros = models.CharField(blank=True, max_length=20)
    commande_stock = models.IntegerField(null=True, blank=True, default="1")
    commande_slug = models.SlugField(null=False, unique=True)
    commande_date = models.DateField(null=True, auto_now_add=True)
    commande_date_update = models.DateField(null=True)
    commande_vues = models.IntegerField(null=True, blank=True, default="0")
    commande_information = models.TextField(null=True, blank=True,max_length=1255)
    commande_valide = models.IntegerField(null=True, blank=True, default="1")
    commande_paiement = models.IntegerField(null=True, blank=True, default="1")
    commande_paiement_reponse =  models.IntegerField(null=True, blank=True, default="1")
    
    commande_utilisateur_id = models.IntegerField(null=True, blank=True, default="1")
    commande_liv_nom = models.CharField(blank=True, max_length=50)
    commande_liv_prenom = models.CharField(blank=True, max_length=50)
    commande_liv_adresse = models.CharField(blank=True, max_length=50)
    commande_liv_ville = models.CharField(blank=True, max_length=50)
    commande_liv_code_postale = models.CharField(blank=True, max_length=50)
    commande_liv_telephone = models.CharField(blank=True, max_length=50)
    commande_liv_email = models.CharField(blank=True, max_length=50)

    commande_fac_nom = models.CharField(blank=True, max_length=50)
    commande_fac_prenom = models.CharField(blank=True, max_length=50)
    commande_fac_adresse = models.CharField(blank=True, max_length=50)
    commande_fac_ville = models.CharField(blank=True, max_length=50)
    commande_fac_code_postale = models.CharField(blank=True, max_length=50)
    commande_fac_telephone = models.CharField(blank=True, max_length=50)
    commande_fac_email = models.CharField(blank=True, max_length=50)

    commande_utilisateur_code_promo = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    
    commande_prix_tva = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    commande_taux_tva = models.DecimalField(max_digits=6, decimal_places=2,default=0, null=True, blank=True)
    commande_prix_ht_hors_liv = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    commande_prix_ttc_hors_liv = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    commande_prix_ht_total = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    commande_prix_ttc_total = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)

    commande_panier_list_id = models.CharField(null=True, blank=True, max_length=1000)

    obj = CommandeManager()
    def __str__(self):
        return self.commande_id

    class Meta:
        indexes = [models.Index(fields=["commande_id", "commande_date","commande_utilisateur_id"], )]
        verbose_name = 'Commande'
class PanierManager(models.Manager):
    pass

class PanierModel(models.Model):
    panier_id = models.AutoField(primary_key=True)
    panier_utilisateur_id = models.IntegerField(null=True, blank=True, default="1")
    panier_titre = models.CharField(null=True,max_length=150)
    panier_produit_id = models.IntegerField(null=True, blank=True, default="1")
    panier_langue = models.CharField(max_length=150)
    panier_url = models.CharField(null=True,max_length=150)
    panier_date = models.DateTimeField(null=True, auto_now_add=True)
    panier_marque = models.CharField(blank=True, max_length=50, null=True)
    panier_vues = models.IntegerField(null=True, blank=True, default="0")
    panier_stock = models.IntegerField(null=True, blank=True, default="1")
    panier_quantite = models.IntegerField(null=True, blank=True, default="1")
    panier_image = models.CharField(blank=True, max_length=150, null=True)
    panier_position = models.CharField(blank=True, max_length=150, null=True)
    panier_couleur = models.CharField(blank=True, max_length=50, null=True)
    panier_taille = models.CharField(blank=True, max_length=50, null=True)
    panier_prix_ttc = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    panier_prix_ht = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    
    panier_prix_ttc_total = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    panier_prix_ht_total = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    
    panier_fichiers1 = models.FileField(null=True, blank=True,upload_to ='telechargement/%d/%m/%Y/')
    
    panier_information = models.TextField(null=True, blank=True,max_length=1255)
    
    obj = PanierManager()
    
    def __str__(self):
        return self.panier_titre

    class Meta:
        indexes = [models.Index(fields=["panier_id", "panier_utilisateur_id","panier_session"], )]
        verbose_name = 'Panier'

class DevisManager(models.Manager):
    pass

class DevisModel(models.Model):
    devis_id = models.AutoField(primary_key=True)
    devis_utilisateur_id = models.IntegerField(null=True, blank=True, default="1")
    devis_langue = models.CharField(null=True, blank=True,max_length=150)
    devis_date = models.DateTimeField(null=True, auto_now_add=True)
    devis_date_update = models.DateField(null=True)

    devis_nom = models.CharField(null=True, blank=True,max_length=150)
    devis_email = models.CharField(max_length=150)
    devis_telephone = models.CharField(null=True, blank=True,max_length=150)
    devis_adresse = models.CharField(null=True, blank=True,max_length=150)
    devis_code_postale = models.CharField(null=True, blank=True,max_length=150)
    devis_ville = models.CharField(null=True, blank=True,max_length=150)
    
    devis_information = models.TextField(null=True, blank=True,max_length=255)
    devis_connu = models.CharField(null=True, blank=True,max_length=150)

    devis_fichiers = models.FileField(null=True, blank=True,upload_to ='telechargement/%d/%m/%Y/')

    obj = DevisManager()
    def __str__(self):
        return f'{ self.devis_email } - {self.devis_information} - {self.devis_email}'

    class Meta:
        indexes = [models.Index(fields=["devis_utilisateur_id", "devis_date", "devis_email"], )]
        verbose_name = 'Devis'
        
        
class LivraisonManager(models.Manager):
    pass

class LivraisonModel(models.Model):
    livraison_id = models.AutoField(primary_key=True)
    livraison_delai = models.IntegerField(null=True, blank=True, default="24")
    livraison_delai_devise = models.CharField(null=True, blank=True,max_length=50)
    livraison_nom = models.CharField(null=True, blank=True,max_length=150)
    livraison_solution = models.CharField(null=True, blank=True,max_length=150)
    livraison_description = models.TextField(null=True, blank=True,max_length=1150)
    livraison_prix_ttc = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)
    livraison_prix_ht = models.DecimalField(max_digits=12, decimal_places=2,default=0, null=True, blank=True)

    
    obj = LivraisonManager()
    def __str__(self):
        return self.livraison_nom

    class Meta:
        indexes = [models.Index(fields=["livraison_nom"], )]
        verbose_name = 'Livraison'
        
class FicheManager(models.Manager):
    pass

class FicheModel(models.Model):
    fiche_id = models.AutoField(primary_key=True)
    fiche_utilisateur_id = models.IntegerField(null=True, blank=True, default="1")
    fiche_langue = models.CharField(max_length=150)
    fiche_slug = models.SlugField(null=False, unique=True)
    fiche_date = models.DateField(null=True, auto_now_add=True)
    fiche_date_update = models.DateField(null=True)

    fiche_nom = models.CharField(max_length=150)
    fiche_email = models.CharField(max_length=150)
    fiche_telephone = models.CharField(max_length=150)
    fiche_adresse = models.CharField(max_length=150)
    fiche_code_postale = models.CharField(max_length=150)
    fiche_ville = models.CharField(max_length=150)
    
    fiche_fichier_slug = models.CharField(max_length=150)
    fiche_fichier_url = models.CharField(max_length=150)
    fiche_solution = models.CharField(max_length=150)
    fiche_information = models.TextField(max_length=255)
    fiche_lieu = models.CharField(max_length=150)

    obj = FicheManager()
    def __str__(self):
        return self.fiche_solution

    class Meta:
        verbose_name = 'Fiche'
