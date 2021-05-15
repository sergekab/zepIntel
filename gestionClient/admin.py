from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *

admin.site.register(Utilisateur)
#admin.site.register(Client)
@admin.register(Client)


class ClientAdmin(ImportExportModelAdmin):
    list_display = ('nom_cl', 'prenom_cl', 'email_cl', 'sexe_cl', 'phone_cl', 'statut_cl', 'date')
    


