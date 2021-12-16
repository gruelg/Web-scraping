from bs4 import BeautifulSoup
import requests
import time

class scrap : 

    def __init__(self) -> None:
        self.url = 'https://www.dureedevie.fr'
        self.plateformes = []
        self.listeJeux = []

    def get_plateforme(self):
        """
            Récupere la liste des jeux sur toutes les plateformes
        """
        r = requests.get(self.url)
        request_text = r.text
        soup = BeautifulSoup(request_text, 'html.parser')
        for a in soup.find_all("a", {"class": "text-lg text-gray-900 font-medium hover:text-gray-600"}) :
            self.plateformes.append([a.text, a.get('href')])
        self.__supprClassement()

    def getDataGames(self):
        #recuperation de la liste des jeux pour toutes les plateformes
        for plateforme in self.plateformes :
            time.sleep(1)
            r = requests.get('{}{}'.format(self.url, plateforme[1]))
            request_text = r.text
            soup = BeautifulSoup(request_text, 'html.parser')
            #pour chaque jeu
            for a in soup.find_all("a", {"class": "underline"}) :
                r = requests.get('{}{}'.format(self.url,a.get('href')))
                request_text = r.text
                soup = BeautifulSoup(request_text, 'html.parser')
                data = []
                for dd in soup.find_all("dd"):
                    data.append(dd.text)
                while len(data) <9 :
                    data.insert(0,'N/A')
                if len(data) == 9 : 
                    self.listeJeux.append([a.text ,plateforme[0], data])

    def __supprClassement(self):
        for i in range(0,13,1):
            self.plateformes.pop(0)

    def getAllData(self):
        self.get_plateforme()
        self.getDataGames()

