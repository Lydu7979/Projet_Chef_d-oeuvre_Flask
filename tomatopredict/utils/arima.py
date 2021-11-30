from utils.MG import data_prix, data_pro, day
import pickle
from datetime import date
import time
timestr = time.strftime("%Y%m%d")
import pandas as pd
import matplotlib.pyplot as plt
import os

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


#Prédiction du prix

def predict_prix_ARIMA():
    chemin4 = os.path.join(os.getcwd(),'tomatopredict','static','images','predicted_values(price)_table(ARIMA).png')
    nprix.savefig(chemin4)
    return 'predicted_values(price)_table(ARIMA).png'

def graph_prix_ARIMA1():
    fig12 = plt.figure(figsize=(10,5))
    plt.plot(forcast, label='prix dans '+ str(day()) +" "+'jours', color = 'darkviolet')
    plt.title("Représentation du prix pour les données prédites")
    plt.xlabel("Jour")
    plt.ylabel("Prix")
    plt.legend(loc="upper right")
    plt.grid(True)
    chemin5 = os.path.join(os.getcwd(),'tomatopredict','static','images','predicted_values(price)_graph(ARIMA).png')
    fig12.savefig(chemin5)
    return 'predicted_values(price)_graph(ARIMA).png'

def graph_prix_ARIMA2():
    fig13 = plt.figure(figsize=(10,5))
    plt.plot(data_prix(), label="prix (valeurs observées)", color = 'darkviolet')
    plt.plot(forcast, label='prix dans '+ str(day()) +" "+'jours', color = 'blue')
    plt.title("Représentation du prix avec les données prédites")
    plt.xlabel("Année")
    plt.ylabel("Prix")
    plt.legend(loc="upper right")
    plt.grid(True)
    chemin6 = os.path.join(os.getcwd(),'tomatopredict','static','images','all_values(price)_graph(ARIMA).png')
    fig13.savefig(chemin6)
    return 'all_values(price)_graph(ARIMA).png'
    

#Prédiction de la production

def predict_production_ARIMA():
    chemin7 = os.path.join(os.getcwd(),'tomatopredict','static','images','predicted_values(production)_table(ARIMA).png')
    n_pro.savefig(chemin7)
    return 'predicted_values(production)_table(ARIMA).png'

def graph_pro_ARIMA1():
    fig14 = plt.figure(figsize=(10,5))
    plt.plot(forcast2, label='production dans '+ str(day()) +" "+'jours', color = 'gold')
    plt.title("Représentation de la production pour les données prédites")
    plt.xlabel("Jour")
    plt.ylabel("Prix")
    plt.legend(loc="upper right")
    plt.grid(True)
    chemin8 = os.path.join(os.getcwd(),'tomatopredict','static','images','predicted_values(production)_graph(ARIMA).png')
    fig14.savefig(chemin8)
    return 'predicted_values(production)_graph(ARIMA).png'

def graph_pro_ARIMA2():
    fig15 = plt.figure(figsize=(10,5))
    plt.plot(data_pro(), label="production (valeurs observées)", color = 'gold')
    plt.plot(forcast2, label='production dans '+ str(day()) +" "+'jours', color = 'blue')
    plt.title("Représentation de la production avec les données prédites")
    plt.xlabel("Année")
    plt.ylabel("Production")
    plt.legend(loc="upper right")
    plt.grid(True)
    chemin9 = os.path.join(os.getcwd(),'tomatopredict','static','images','all_values(production)_graph(ARIMA).png')
    fig15.savefig(chemin9)
    return 'all_values(production)_graph(ARIMA).png'