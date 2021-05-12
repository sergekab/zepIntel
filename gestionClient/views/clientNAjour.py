from django.shortcuts import render, redirect
from django.views import View
from gestionClient.models.client import Client

from django.core.paginator import Paginator
import xlwt
 

class Index(View):
    def post(self, request):
        return redirect('client_non_a_jour')


    def get(self, request):

        data = {}

        clientsAj = Client.get_all_clientNAJ()

        #pour la pagination
        paginator=Paginator(clientsAj, 6)
        page_number = request.GET.get("page")
        page_obj = Paginator.get_page(paginator, page_number)
        data['page_obj'] = page_obj

       
        return render(request, 'clientAjour.html', data)


def deleteCustomer(request, id):
    clientById = Client.objects.get(pk=id)
    clientById.delete()
    return redirect('client_non_a_jour')

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

    rows = Client.get_all_clientNAJ().values_list('id', 'nom_cl', 'prenom_cl', 'sexe_cl', 'phone_cl', 'email_cl', 'date', 'statut_cl')

    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

      
    return response































def addCustomer():
    pass
    return redirect('homepage')

def editCustomer(request, id):
    pass
    return redirect('homepage')