from django.db import models
from .client import Client

class Souscription(models.Model):
    date = models.CharField(max_length=100)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)


    def souscription(self):
        self.save()

        
    @staticmethod
    def get_souscriptionByClient(client):
        return Souscription.objects.get(client=client)

    @staticmethod
    def get_souscription():
        return Souscription.objects.all()




