import requests
from requests.structures import CaseInsensitiveDict
import json


class Api:

    def __init__(self):
        self.urlPost = 'https://dev.synerboard.com/serverBeer/rest/smartFinal/addSmart'
        self.urlGet = 'https://dev.synerboard.com/serverBeer/rest/smartFinal/getSmart'
        self.urlDelete = 'https://dev.synerboard.com/serverBeer/rest/smartFinal/deleteAll'
        self.urlUpdate = 'https://dev.synerboard.com/serverBeer/rest/smartFinal/updateSmart'

    def metodoPost(self,request):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        response = requests.post(self.urlPost,request)
        return response.json()

    def metodoDelete(self):
        try:
            response = requests.delete(self.urlDelete)
            return response.json()
        except:
            return "ocurrio un error"
        