# gold_ons_price_predictor/model.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM


def create_model(seq_length):
    model = Sequential([
        LSTM(50, activation='relu', input_shape=(seq_length, 1)),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.summary()
    return model


def train_model(model, X_train, y_train, X_val, y_val, epochs=20):
    history = model.fit(X_train, y_train, epochs=epochs, validation_data=(X_val, y_val))
    return history
