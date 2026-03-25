
from django.db import models


class UtilisateurManager(models.Manager):
    pass

class UtilisateurModel(models.Model):
   
    utilisateur_nom = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_prenom = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_email = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_adresse= models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_code_postale = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_ville = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_pays = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_langue = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_telephone = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_passion = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_siren = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_kbis= models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_entreprise = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_sesssion = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_valide = models.CharField(max_length=1024,null=True, blank=True)
    utilisateur_groupe = models.CharField(max_length=1024,null=True, blank=True)
  
    obj = UtilisateurManager()
    
    def __str__(self):
        return self.utilisateur_nom

    class Meta:
        verbose_name = 'utilisateur'
