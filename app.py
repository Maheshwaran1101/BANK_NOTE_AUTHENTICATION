import uvicorn
from fastapi import FastAPI
from Banknote import Banknote

import pickle
import numpy as np
import pandas as pd

app = FastAPI() 
pickle_in = open('classifier.pkl', 'rb')  #open the file in read binary mode to load the model
classifier = pickle.load(pickle_in)  #load the model from the file

@app.post('/predict')
def predict_banknote(data:Banknote):   #from Banknote import Banknote is used to import the Banknote class from the Banknote.py file which is used for data validation and parsing and also it will convert the input data into the format required by the model for making predictions.
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5001)
    
    
"""
in output

0 = Fake
1 = Real

"""
