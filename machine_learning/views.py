from django.shortcuts import render
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle  

#Loading the trained model 
with open('/home/motabo/Documents/model/model.pkl', 'rb') as f:
    model_lr = pickle.load(f)


def predict(request):
    file_path = 'machine_learning/records.csv'
    df = pd.read_csv(file_path)
    x =  df.drop("disposal",axis=1)
    y = df["disposal"]
    scalar = StandardScaler()
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)


    prediction = model_lr.predict(x_test)[45]

    # Pass prediction to template
    context = {'prediction': prediction}
    return render(request, 'machine_learning/predict.html', context)
