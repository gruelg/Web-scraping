from classes.scrap import scrap 
from classes.cleaning import cleaning
from classes.stats import stats 
from classes.graph import graph
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--methode', dest='methode', type=str, help='methode', metavar='methode', default='scrapping')
args = parser.parse_args()

if args.methode == "scrapping":
    jeux = scrap()
    jeux.getAllData()
    data = cleaning(jeux.listeJeux)
    data.cleaning()
    dataframe = data.df
    print(dataframe.dtypes) 

if args.methode == "csv" :
    dataframe = pd.read_csv('dataframe.csv',sep=';')

stat = stats(dataframe)
stat.getAllStats()

graphs = graph(dataframe)
graphs.getAllGraphes()
