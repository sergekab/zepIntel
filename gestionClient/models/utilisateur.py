from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10000)


    @staticmethod
    def get_utilisateur_by_name(username):

        try:
            return Utilisateur.objects.get(username = username)
        except:
            return False

    @staticmethod
    def get_agent_by_id(id):
        try:
            return Utilisateur.objects.get(id = id)
        except:
            return False
       

    def isExists(self):
        if Utilisateur.objects.filter(username = self.username):
            return True

        return False

    def __str__(self):
        return self.nom +" "+ self.prenom + " "