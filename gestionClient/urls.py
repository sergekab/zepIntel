from django.urls import path
from .views import login, home, clientAjour, clientNAjour



urlpatterns = [

    path('', login.Login.as_view(), name='login'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.logout, name='logout'),
    path('homepage', home.Index.as_view(), name='homepage'),
    path('saveCl', home.addCustomer, name='saveCl'),
    path('exportExcel', home.exportXsl, name='exportExcel'),
    path('client_a_jour', clientAjour.Index.as_view(), name='client_a_jour'),
    path('client_non_a_jour', clientNAjour.Index.as_view(), name='client_non_a_jour'),

    path('exportExcel', clientAjour.exportXsl, name='exportExcel'),
    path('exportExcel', clientNAjour.exportXsl, name='client_non_a_jour'),
     path('edit/<int:id>', home.editCustomer, name='edit'),
    path('delete/<int:id>', home.deleteCustomer, name='delete'),
    path('modifier_statut/<int:id>', home.modifierStatut, name='modifier_statut'),
    path('update/<int:id>', home.update, name='update'),

    path('upload', home.importXls, name='upload'),
]