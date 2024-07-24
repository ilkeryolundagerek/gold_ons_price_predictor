import unittest
from gold_ons_price_predictor.data_preparation import load_data, create_sequences
from gold_ons_price_predictor.model import create_model, train_model
from gold_ons_price_predictor.predict import predict_next_value


class TestGoldOnsPricePredictor(unittest.TestCase):
    def test_predict(self):
        data = load_data('data/gold_ons_prices.csv')
        SEQ_LENGTH = 20
        X, y = create_sequences(data, SEQ_LENGTH)
        split = int(len(X) * .8)
        X_train, X_test = X[:split], X[split:]
        y_train, y_test = y[:split], y[split:]
        X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
        X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
        model = create_model(SEQ_LENGTH)
        train_model(model, X_train, y_train, X_test, y_test, 1)
        prediction = predict_next_value(model, data, SEQ_LENGTH)
        self.assertIsInstance(prediction, float)


if __name__ == '__main__':
    unittest.main()
