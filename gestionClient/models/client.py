from django.db import models

class Client(models.Model):
    #id_sur = models.IntegerField(primary_key=True)
    nom_cl = models.CharField(max_length=100)
    prenom_cl = models.CharField(max_length=100)
    email_cl = models.EmailField()
    sexe_cl = models.CharField(max_length=50)
    phone_cl = models.CharField(max_length=50)
    statut_cl = models.BooleanField(default=False)
    date = models.CharField(max_length=100)

    def clientSave(self):
        self.save()

    def clientdel(self):
        self.delete()
        

    @staticmethod
    def isExist(email):
        try:
            Client.objects.get(email_cl = email)
            return True
        except:
            return False

    @staticmethod
    def get_all_client():
        return Client.objects.all()

    @staticmethod
    def get_all_clientAJ():
        return Client.objects.filter(statut_cl=True)

    @staticmethod
    def get_all_clientNAJ():
        return Client.objects.filter(statut_cl=False)