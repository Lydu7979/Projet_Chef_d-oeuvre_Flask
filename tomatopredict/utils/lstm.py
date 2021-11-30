from utils.MG import data_prix, data_pro, day, data
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from keras.models import load_model
from datetime import date
import time
timestr = time.strftime("%Y%m%d")
import pandas as pd
import numpy as np
import os

scaler = MinMaxScaler()
scaler2 = MinMaxScaler()

mod3 = load_model('prediction_prix_tomate_lstm_model_v1.h5')

mod4 = load_model('prediction_production_tomate_lstm_model_v1.h5')

D1 = pd.read_csv("./DATA/TMN.csv", parse_dates=['Date'], dayfirst= True)
D1.sort_values(by=['Date'], inplace=True, ascending=True) 
D1 =  D1.set_index(['Date'])
D2 = D1.resample("D").mean()
D2 = D2.interpolate()
Pop3 = D2[['prix moyen au kg','Production quantité tonne(s)']]

lstm_prix = Pop3.filter(['prix moyen au kg'])
lstm_pro = Pop3.filter(['Production quantité tonne(s)'])

seq = 7 # nombre dobservations dans une séquence
n_fe = 1 # nombre de features pour le modèle

x = len(lstm_prix) - 14

train = lstm_prix.iloc[:x]
test = lstm_prix.iloc[x:]
scaler.fit(train)
train_s = scaler.transform(train)
test_s = scaler.transform(test)

x2 = len(lstm_pro) - 14

train2 = lstm_pro.iloc[:x2]
test2 = lstm_pro.iloc[x2:]
scaler2.fit(train2)
train_s2 = scaler2.transform(train2)
test_s2 = scaler2.transform(test2)

def graph_pred_prix_lstm():
    prediction_prix = []
    ca1 = train_s[-seq:]
    ca1 = ca1.reshape(1, seq, n_fe)
    future = day()
    for i in range(len(test) + future):
        cp1 = mod3.predict(ca1)[0]
        prediction_prix.append(cp1)
        ca1 = np.append(ca1[:,1:,:],[[cp1]],axis=1)
    
    pred1 = scaler.inverse_transform(prediction_prix)
    ts1 = test.index
    for j in range(0, future):
        ts1 = ts1.append(ts1[-1:] + pd.DateOffset(1))
    
    Pred_prix = pd.DataFrame(columns = ['prix actuel', 'prix prédit'], index=pd.date_range(start=date.today(),periods=future, freq='D'))
    Pred_prix.loc[:,'prix prédit'] = pred1[:,0]
    Pred_prix.loc[:,'prix actuel'] = test["prix moyen au kg"]
    Ppi = Pred_prix['prix prédit'].tail(future)
    chemin12 = os.path.join(os.getcwd(),'tomatopredict','static','images','predicted_values(price)_table(LSTM).png')
    Ppi.savefig(chemin12)
    Ppi2 = Ppi.plot(title = 'Prédiction du prix dans '+ str(future) +" "+' jours')
    chemin10 = os.path.join(os.getcwd(),'tomatopredict','static','images','predicted_values(price)_graph(LSTM).png')
    Ppi2.savefig(chemin10)
    return 'predicted_values(price)_table(LSTM).png' and 'predicted_values(price)_graph(LSTM).png'

def graph_pred_pro_lstm():
    prediction_pro = []
    ca2 = train_s2[-seq:]
    ca2 = ca2.reshape(1, seq, n_fe)
    future = day()
    for i in range(len(test2) + future):
        cp2 = mod4.predict(ca2)[0]
        prediction_pro.append(cp2)
        ca2 = np.append(ca2[:,1:,:],[[cp2]],axis=1)
    
    pred2 = scaler.inverse_transform(prediction_pro)
    ts2 = test2.index
    
    for j in range(0, future):
        ts2 = ts2.append(ts2[-1:] + pd.DateOffset(1))

    Pred_pro = pd.DataFrame(columns = ['production actuelle', 'production prédite'], index = pd.date_range(start=date.today(),periods=future, freq='D'))
    Pred_pro.loc[:,'production prédite'] = pred2[:,0]
    Pred_pro.loc[:,'production actuelle'] = test2["Production quantité tonne(s)"]
    Po = Pred_pro['production prédite'].tail(future)
    chemin13 = os.path.join(os.getcwd(),'tomatopredict','static','images','predicted_values(production)_table(LSTM).png')
    Po.savefig(chemin13)
    Po2 = Po.plot(title = 'Prédiction de la production dans '+ str(future) +" "+' jours')
    chemin11 = os.path.join(os.getcwd(),'tomatopredict','static','images','predicted_values(production)_graph(LSTM).png')
    Po2.savefig(chemin11)
    return 'predicted_values(production)_table(LSTM).png' and  'predicted_values(production)_graph(LSTM).png'


