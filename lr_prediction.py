import pickle
import pandas as pd


def pred(json_file):
    with open('static/lr_model.pkl', 'rb') as f:
        model = pickle.load(f)
    df = pd.read_json(json_file)
    json_file['rd'] = model.predict(df)[0]
    print(json_file['rd'])
    return json_file


