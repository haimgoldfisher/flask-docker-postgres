import pickle
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

def pred(json_file):
    with open('static/lr_model.pkl', 'rb') as f:
        model = pickle.load(f)
    df = pd.DataFrame([json_file])
    prediction = model.predict(df)
    return prediction[0]


