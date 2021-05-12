from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import *
from django.views import View
from gestionClient.models.client import Client

from django.core.paginator import Paginator
import xlwt
 

class Index(View):
    def post(self, request):
        return redirect('homepage')


    def get(self, request):

        data = {}

        clients = Client.get_all_client()
        clientsAj = Client.get_all_clientAJ()
        clientsNAj = Client.get_all_clientNAJ()        

        #pour la pagination
        paginator=Paginator(clients, 6)
        page_number = request.GET.get("page")
        page_obj = Paginator.get_page(paginator, page_number)
        data['page_obj'] = page_obj
       
        return render(request, 'index.html', data)


def deleteCustomer(request, id):
    clientById = Client.objects.get(pk=id)
    clientById.delete()
    return redirect('homepage')



def modifierStatut(request, id):
    clientById = Client.objects.get(pk=id)

    if clientById.statut_cl == False:
        clientById.statut_cl = True
        clientById.clientSave()
    else:
        clientById.statut_cl = False
        clientById.clientSave()
    return redirect('homepage')




def addCustomer(request):
    nom = request.POST.get('nom_cl')
    prenom = request.POST.get('prenom_cl')
    sexe = request.POST.get('sexe_cl')
    email = request.POST.get('email_cl')
    phone = request.POST.get('contact_cl')
    date = request.POST.get('date')


    message = None
    data = {}

    client = Client(
        nom_cl=nom,
        prenom_cl=prenom,
        sexe_cl=sexe,
        phone_cl=phone,
        email_cl=email,
        date = date
    )
    client.clientSave()
    return redirect('homepage')



def editCustomer(request, id):
    pass
    return redirect('homepage')


def exportXsl(request):
    response = HttpResponse(content_type = 'ms-excel')
    response['Content-Disposition'] = 'attachement; filename=Clients'+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Clients')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id', 'Nom', 'Prenom', 'Sexe', 'Téléphone', 'Email', 'Date de Souscription', 'Statut']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Client.get_all_client().values_list('id', 'nom_cl', 'prenom_cl', 'sexe_cl', 'phone_cl', 'email_cl', 'date', 'statut_cl')

    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

      
    return response