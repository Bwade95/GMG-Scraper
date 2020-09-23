import os, requests

class GMGaming:
    def __init__(self,search_term):
        self.search_term = search_term

    def set_url(self):
        return f"https://www.greenmangaming.com/search/{self.search_term}"
    
    def make_request(self):
        url = self.set_url()
        return requests.request("GET", url)

gmg = GMGaming("Mafia")