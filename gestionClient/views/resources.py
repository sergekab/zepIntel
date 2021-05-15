from import_export import resources
from gestionClient.models.client import Client


class ClientResource(resources.ModelResource):
    class meta:
        model = Client