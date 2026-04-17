import pandas as pd

def predict_demand(model, columns, data):
    data = pd.get_dummies(data)
    data = data.reindex(columns=columns, fill_value=0)
    return model.predict(data).tolist()

def predict_delay(model, columns, data):
    data = pd.get_dummies(data)
    data = data.reindex(columns=columns, fill_value=0)
    return model.predict_proba(data)[:, 1].tolist()