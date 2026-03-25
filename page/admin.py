from django.contrib import admin
from page.models import PageModel, EvenementModel

admin.site.register([PageModel, EvenementModel])