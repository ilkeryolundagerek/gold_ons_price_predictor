# gold_ons_price_predictor/predict.py
def predict_next_value(model, data, seq_length):
    last_seq = data[-seq_length:].values
    last_seq = last_seq.reshape((1, seq_length, 1))
    next_val = model.predict(last_seq)
    return next_val[0][0]
