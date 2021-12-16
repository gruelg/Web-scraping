import pandas as pd

class cleaning :

    def __init__(self, data) :
        self.data = data
        self.df = {}

    def toDataframe(self):
        d = { 'titre': [self.data[i][0] for i in range(len(self.data))],
        'Temps de jeu moyen' : [self.data[i][2][0] for i in range(len(self.data))],
        'Histoire  Trame principale' : [self.data[i][2][1] for i in range(len(self.data))],
        'Histoire + Quêtes secondaires' : [self.data[i][2][2] for i in range(len(self.data))],
        'Complétionniste (100%)' : [self.data[i][2][3] for i in range(len(self.data))],
        'Genres' : [self.data[i][2][4] for i in range(len(self.data))],
        'Plateformes' : [self.data[i][1] for i in range(len(self.data))],
        'Développeur' : [self.data[i][2][6] for i in range(len(self.data))],
        'Editeur' : [self.data[i][2][7] for i in range(len(self.data))],
        'Date de sortie' : [self.data[i][2][8] for i in range(len(self.data))]
        }
        self.df = pd.DataFrame(data=d)
    
    def datetoDatetime(self):
        self.df['Date de sortie'] = pd.to_datetime(self.df['Date de sortie'], format='%d/%m/%Y',errors='coerce')
    
    def convertTempsJeuInt(self):
        for colonne in ['Temps de jeu moyen','Histoire  Trame principale','Histoire + Quêtes secondaires','Complétionniste (100%)'] :
            self.df[colonne] = pd.to_numeric(self.df[colonne].str.replace('h', '.', regex=True),errors='coerce')
    
    def exportCSV(self):
        self.df.to_csv(r'dataframe.csv',sep=';')

    def cleaning(self):
        self.toDataframe()
        self.datetoDatetime()
        self.convertTempsJeuInt()
        self.exportCSV()