from utils.MG import data_prix, data_pro, day
import pickle
from datetime import date
import time
timestr = time.strftime("%Y%m%d")
import pandas as pd
import matplotlib.pyplot as plt

mod = pickle.load(open('modèle_ARIMA_Prix3.pkl', 'rb'))
			
mod2 = pickle.load(open('modèle_ARIMA_Production3.pkl', 'rb'))

#prix
forecast,err,ci = mod.forecast(steps= day(), alpha = 0.05)
nprix = pd.DataFrame({"Date":pd.date_range(start= date.today(), periods=day(), freq='D'), 'prix dans '+ str(day()) +" "+'jours' :list(forecast)})
df_forecast = pd.DataFrame({'Prix dans '+  str(day()) +" "+'jours' :forecast},index=pd.date_range(start=date.today(), periods=day(), freq='D'))
df_forecast.to_csv("Forecast.csv")
forcast=pd.read_csv('Forecast.csv')	
forcast.rename(columns={"Unnamed: 0": "Date",'Prix dans '+ str(day()) +" "+'jours':"prix moyen au kg"},inplace=True)
forcast['Date'] = pd.to_datetime(forcast['Date'],infer_datetime_format=True)
forcast.index=forcast['Date']
del forcast['Date']
fig1 = pd.concat([data_prix,forcast])

#production
forecast2,err,ci = mod2.forecast(steps= day(), alpha = 0.05)
df_forecast2 = pd.DataFrame({'Production dans '+ str(day()) +" "+'jours' :forecast2},index=pd.date_range(start=date.today(),periods=day(), freq='D'))
n_pro = pd.DataFrame({"Date":pd.date_range(start=date.today(), periods=day(), freq='D'),'production dans '+ str(day()) +" "+'jours' :list(forecast2)})
df_forecast2.to_csv("Forecast2.csv")
forcast2=pd.read_csv('Forecast2.csv')
forcast2.rename(columns={"Unnamed: 0": "Date",'Production dans '+ str(day()) +" "+'jours':"Production quantité tonne(s)"},inplace=True)
forcast2.head()
forcast2['Date'] = pd.to_datetime(forcast2['Date'],infer_datetime_format=True)
forcast2.index=forcast2['Date']
del forcast2['Date']
fig4 = pd.concat([data_pro,forcast2])

#Prédiction du prix

def predict_prix_ARIMA():
    nprix.savefig('static/images/Données prédites(Prix).png')
    return nprix

def graph_prix_ARIMA1():
    fig12 = plt.figure(figsize=(10,5))
    plt.plot(forcast, label='prix dans '+ str(day()) +" "+'jours', color = 'darkviolet')
    plt.title("Représentation du prix pour les données prédites")
    plt.xlabel("Jour")
    plt.ylabel("Prix")
    plt.legend(loc="upper right")
    plt.grid(True)
    fig12.savefig("static/images/Représentation du prix (données prédites).png")
    return fig12

def graph_prix_ARIMA2():
    fig13 = plt.figure(figsize=(10,5))
    plt.plot(data_prix(), label="prix (valeurs observées)", color = 'darkviolet')
    plt.plot(forcast, label='prix dans '+ str(day()) +" "+'jours', color = 'blue')
    plt.title("Représentation du prix avec les données prédites")
    plt.xlabel("Année")
    plt.ylabel("Prix")
    plt.legend(loc="upper right")
    plt.grid(True)
    fig13.savefig("static/images/Représentation du prix (données prédites et données prédites).png")
    return fig13

#Prédiction de la production

def predict_production_ARIMA():
    n_pro.savefig('static/images/Données prédites(Production).png')
    return n_pro

def graph_pro_ARIMA1():
    fig14 = plt.figure(figsize=(10,5))
    plt.plot(forcast2, label='production dans '+ str(day()) +" "+'jours', color = 'gold')
    plt.title("Représentation de la production pour les données prédites")
    plt.xlabel("Jour")
    plt.ylabel("Prix")
    plt.legend(loc="upper right")
    plt.grid(True)
    fig14.savefig("static/images/Représentation de la production (données prédites).png")
    return fig14

def graph_pro_ARIMA2():
    fig15 = plt.figure(figsize=(10,5))
    plt.plot(data_pro(), label="production (valeurs observées)", color = 'gold')
    plt.plot(forcast2, label='production dans '+ str(day()) +" "+'jours', color = 'blue')
    plt.title("Représentation de la production avec les données prédites")
    plt.xlabel("Année")
    plt.ylabel("Production")
    plt.legend(loc="upper right")
    plt.grid(True)
    fig15.savefig("static/images/Représentation de la production (données historiques et données prédites).png")
    return fig15