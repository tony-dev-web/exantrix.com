from django.db import models




class PageModel(models.Model):
    page_id = models.AutoField(primary_key=True)
    page_url = models.CharField(max_length=1024,null=True, blank=True)
    page_titre = models.CharField(max_length=60,null=True, blank=True)
    page_slug = models.CharField(max_length=1024,null=True, blank=True)
    page_description = models.CharField(max_length=260,null=True, blank=True)
    page_categorie = models.CharField(max_length=1024,null=True, blank=True)
    page_langue = models.CharField(max_length=1024,null=True, blank=True)

    def __str__(self):
        return self.page_h1

    class Meta:
        verbose_name = 'page'
        indexes = [models.Index(fields=["page_id","page_url","page_slug","page_noindex"])]
        
class EvenementModel(models.Model):
    evenement_id = models.AutoField(primary_key=True)
    evenement_url = models.CharField(max_length=1024,null=True, blank=True)
    evenement_titre = models.CharField(max_length=60,null=True, blank=True)
    evenement_slug = models.CharField(max_length=1024,null=True, blank=True)
    evenement_description = models.CharField(max_length=260,null=True, blank=True)
    evenement_information = models.CharField(max_length=10000,null=True, blank=True)
    evenement_keywords = models.CharField(max_length=1024,null=True, blank=True)
    evenement_categorie = models.CharField(max_length=1024,null=True, blank=True)
    evenement_langue = models.CharField(max_length=1024,null=True, blank=True)
    evenement_date = models.DateField(null=True, auto_now_add=True)
    
    evenement_date_debut = models.DateField(null=True, auto_now_add=True)
    evenement_date_fin = models.DateField(null=True, auto_now_add=True)
    
    def __str__(self):
        return self.evenement_h1

    class Meta:
        verbose_name = 'evenement'
        indexes = [models.Index(fields=["evenement_id","evenement_url","evenement_slug"])]