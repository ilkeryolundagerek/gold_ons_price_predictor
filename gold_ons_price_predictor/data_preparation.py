# gold_ons_price_predictor/data_preparation.py
import pandas as pd
import numpy as np


def load_data(file_path):
    data = pd.read_csv('XAUUSD_1D_modified.csv')
    return data['close'].values


def create_sequences(data, seq):
    xs, ys = [], []
    for i in range(len(data) - seq - 1):
        x = data[i:i + seq]
        y = data[i + seq]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)
