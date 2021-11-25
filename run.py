print('Hello')
import datetime
from flask import Flask, jsonify, request, render_template, redirect, url_for
from pathlib import Path
import os.path
import pytest
import pandas as pd
import numpy as np
import sqlite3
import hashlib
import matplotlib.pyplot as plt
import warnings                                  
warnings.filterwarnings('ignore')
import pymongo
from datetime import date
import base64 
import time
timestr = time.strftime("%Y%m%d")
import dns
from Sécurité.Safe import modi, verif
from sklearn.preprocessing import MinMaxScaler
import pickle
import datetime 
from Pages_db.Admin import admin
from app import db
from Base_données.DBMongo import get_client_mongodb
import dns
import pymongo
import pandas as pd

mod = pickle.load(open('modèle_ARIMA_Prix3.pkl', 'rb'))
			

mod2 = pickle.load(open('modèle_ARIMA_Production3.pkl', 'rb'))



app2 = Flask(__name__)

app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///<user>.db'
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app2.secret_key = 'xyzdrrrretetetetetete'

client = get_client_mongodb()

db2 = client.Tomates_meteo_Centre8
mycl = db2["données"]
Dat = pd.DataFrame(list(mycl.find()))
Dat = Dat.drop(columns=["index"])
print(Dat) #pour afficher la base de données sous forme de dataframe
DT = pd.DataFrame(Dat, columns = ['Date', 'prix moyen au kg', 'Production quantité \ntonne(s)', 'Température minimale en °C', 
                              'Température maximale en °C', 'précipitations en mm','Ensoleillement en min', 'Rafales (vitesse du vent) en km/h','catégorie tomates'])
DT.rename(columns={"Production quantité \ntonne(s)": "Production quantité tonne(s)"},inplace=True)
DT.to_csv('DATA/TMN.csv',index = False)

Pop = pd.read_csv("/Data/TMN.csv", parse_dates=['Date'], dayfirst= True)
Pop.sort_values(by=['Date'], inplace=True, ascending=True) 
Pop = Pop.set_index(['Date'])
Pop2 = Pop.resample("D").mean()
Pop2 = Pop2.interpolate()
Pop3 = Pop2[['prix moyen au kg','Production quantité tonne(s)']] 
print(Pop3)


scaler = MinMaxScaler()
				
Pop3[['prix_n', 'production_n']] = scaler.fit_transform(Pop3[['prix moyen au kg', 'Production quantité tonne(s)']])

data = Pop3.filter(['prix moyen au kg'])
data2 = Pop3.filter(['Production quantité tonne(s)'])


def graph1():
    fig = plt.figure(figsize=(10,5))
    plt.plot(Pop3.prix_n, label="prix normalisé", color = 'darkviolet')
    plt.plot(Pop3.production_n, label="production normalisée", color = 'gold')
    plt.title("Représentation du prix au kilo et de la production")
    plt.legend(loc="upper right")
    plt.grid(True)
    fig.savefig("static/images/Représentation du prix au kilo et de la production.png")

def graph2():
    fig2 = plt.figure(figsize=(10,5))
    plt.plot(data, label="prix au kilo", color = 'darkviolet') 
    plt.title("Représentation du prix au kilo au cours du temps")
    plt.xlabel("Année")
    plt.ylabel("Prix")
    plt.legend(loc="upper right")
    plt.grid(True)
    fig2.savefig("static/images/Représentation du prix au kilo.png")

def graph3():
    fig3 = plt.figure(figsize=(10,5))
    plt.plot(data2, label="production", color = 'darkviolet') 
    plt.title("Représentation de la production au cours du temps")
    plt.xlabel("Année")
    plt.ylabel("Production")
    plt.legend(loc="upper right")
    plt.grid(True)
    fig3.savefig("static/images/Représentation du production.png")



app2.run(host='localhost', port=5000)

@app2.before_first_request
def create_all():
    db.create_all()


if __name__ == "__main__":
    app2.run(debug=True)