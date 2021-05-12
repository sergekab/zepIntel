from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password, make_password
from gestionClient.models.utilisateur import Utilisateur
from django.views import View

class Login(View):

    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        utilisateur = Utilisateur.get_utilisateur_by_name(username)

        error_message = None

        if utilisateur:
            if password == utilisateur.password:
                request.session['utilisateur_id'] = utilisateur.id
                
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')


                #request.session['email'] = customer.email
                return redirect('homepage')

            else:
                error_message = 'Nom d\'utilisateur ou mot de passe invalide'

        else:
            error_message = 'Nom d\'utilisateur ou mot de passe invalide'

        return render(request, 'login.html', {'error' : error_message})
         

def logout(request):
    request.session.clear()
    return redirect('login')