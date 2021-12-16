import pandas as pd

class stats :

    def __init__(self, data) -> None:
        self.df = data

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
        self.nbJeuPlateforme()
        self.minTempsJeu()
        self.moyenneTempsJeu()
        self.maxTempsJeu()