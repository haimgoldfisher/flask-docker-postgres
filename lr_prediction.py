import pickle
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

def pred(data):
    with open('static/lr_model.pkl', 'rb') as f:
        model = pickle.load(f)
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return prediction[0]