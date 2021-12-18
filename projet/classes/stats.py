import pandas as pd

class stats :

    def __init__(self, data) -> None:
        self.df = data

    def datetoDatetime(self):
        self.df['Date de sortie'] = pd.to_datetime(self.df['Date de sortie'], format='%d/%m/%Y',errors='coerce')

    def nbJeuPlateforme(self):
        self.df['Date de sortie'].dt.year.value_counts().sort_index()

    def minTempsJeu(self):
        for colonne in ['Temps de jeu moyen','Histoire  Trame principale','Histoire + Quêtes secondaires','Complétionniste (100%)'] :
            print('min de {} : {} '.format(colonne,self.df[colonne].min()))

    def moyenneTempsJeu(self):
        for colonne in ['Temps de jeu moyen','Histoire  Trame principale','Histoire + Quêtes secondaires','Complétionniste (100%)'] :
            print('moyenne de {} : {} '.format(colonne,self.df[colonne].mean()))

    def maxTempsJeu(self):
        for colonne in ['Temps de jeu moyen','Histoire  Trame principale','Histoire + Quêtes secondaires','Complétionniste (100%)'] :
            print('max de {} : {} '.format(colonne,self.df[colonne].max()))

    def getAllStats(self):
        self.datetoDatetime()
        self.nbJeuPlateforme()
        self.minTempsJeu()
        self.moyenneTempsJeu()
        self.maxTempsJeu()