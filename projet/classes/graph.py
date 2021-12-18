import pandas as pd
import matplotlib.pyplot as plt

class graph:

    def __init__(self, data) -> None:
        self.df = data

    def nbJeuAnnee(self):
        nbJeux = self.df['Date de sortie'].dt.year.value_counts().sort_index().tolist()
        annee = self.df['Date de sortie'].dt.year.value_counts().sort_index().keys().tolist()
        plt.bar(annee, nbJeux )
        plt.xlabel('annee')
        plt.ylabel('nb jeux')
        plt.title('nombre de jeux/an')       
        plt.savefig('graphiques/nbJeuAnnee.png')
    
    def minTempsPlateform(self):
        data = 220
        plt.figure(figsize=(25,25))
        for colonne in ['Temps de jeu moyen','Histoire  Trame principale','Histoire + Quêtes secondaires','Complétionniste (100%)'] :
            data+=1
            plt.subplot(data)
            plt.xlabel('plateformes')
            plt.ylabel('temps(h)')
            plt.title(colonne)
            plt.xticks(rotation=45, ha='right')   
            plt.bar(self.df[colonne].groupby(self.df['Plateformes']).min().keys().tolist(),self.df[colonne].groupby(self.df['Plateformes']).min().tolist() )
            plt.savefig('graphiques/minTempsPlateform.png')

    def moyenneTempsPlateform(self):
        data = 220
        plt.figure(figsize=(25,25))
        for colonne in ['Temps de jeu moyen','Histoire  Trame principale','Histoire + Quêtes secondaires','Complétionniste (100%)'] :
            data+=1
            plt.subplot(data)
            plt.xlabel('plateformes')
            plt.ylabel('temps(h)')
            plt.title(colonne)
            plt.xticks(rotation=45, ha='right')   
            plt.bar(self.df[colonne].groupby(self.df['Plateformes']).mean().keys().tolist(),self.df[colonne].groupby(self.df['Plateformes']).mean().tolist() )
            plt.savefig('graphiques/moyenneTempsPlateform.png')

    def maxTempsPlateform(self):
        data = 220
        plt.figure(figsize=(25,25))
        for colonne in ['Temps de jeu moyen','Histoire  Trame principale','Histoire + Quêtes secondaires','Complétionniste (100%)'] :
            data+=1
            plt.subplot(data)
            plt.xlabel('plateformes')
            plt.ylabel('temps(h)')
            plt.title(colonne)
            plt.xticks(rotation=45, ha='right')   
            plt.bar(self.df[colonne].groupby(self.df['Plateformes']).max().keys().tolist(),self.df[colonne].groupby(self.df['Plateformes']).max().tolist() )
            plt.savefig('graphiques/maxTempsPlateform.png')

    def getAllGraphes(self):
        self.nbJeuAnnee()
        self.minTempsPlateform()
        self.moyenneTempsPlateform()
        self.maxTempsPlateform()