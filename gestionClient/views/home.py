from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import *
from django.views import View
from gestionClient.models.client import Client

from django.core.paginator import Paginator
import xlwt
from .resources import ClientResource
#from gestionClient.resources.py import ClientResource
from tablib import Dataset

 

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
    data = {}
    clientById = Client.objects.get(pk=id)
    data['clientById'] = clientById
    
    return render(request, 'edit.html', data)

def update(request, id):

    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    sexe = request.POST.get('sexe')
    email = request.POST.get('email')
    phone = request.POST.get('contact')
    date = request.POST.get('date')

    print(nom, prenom, sexe, email, phone, date)

    clientById = Client.objects.get(pk=id)
    
    clientById.nom_cl = str(nom),
    # clientById.prenom_cl = str(prenom),
    # clientById.sexe_cl = str(sexe),
    # clientById.email_cl = str(email),
    # clientById.phone_cl = str(phone),
    # clientById.date = str(date)
    
    #clientById.save()
    print(str(clientById.nom_cl))
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

def importXls(request):

    if request.method == "POST":
        import_file = request.FILES['myfile']
        from xlrd import open_workbook
        wb = open_workbook(file_contents=import_file.read())
        data = list()
        for s in wb.sheets():
            print ('Sheet:', s.name)
            for row in range(s.nrows):
                if row > 0:
                    values = []
                    for column in range(s.ncols):
                        values.append(str(s.cell(row, column).value))
                    data.append(values)                   
                    for element in data:
                        isExist = Client.isExist(element[5])

                        if isExist == False:
                            client = Client(
                                nom_cl=element[1],
                                prenom_cl=element[2],
                                sexe_cl=element[3],
                                phone_cl=element[4],
                                email_cl=element[5],
                                date = element[6],
                                statut_cl=element[7]
                            )
                            client.clientSave()
                        else:
                            pass
    return redirect('homepage')
