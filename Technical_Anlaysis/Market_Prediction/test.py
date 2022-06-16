import pandas as pd
from pandas_datareader import data
import numpy as np

class test:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()

        self.prediction_frame = data_frame.get_basic().copy(deep=True)
        print(34)
        print(self.prediction_frame)


    def create_classification_trading_condition(self):
     self.prediction_frame['Open-Close'] =  self.prediction_frame.Open -  self.prediction_frame.Close
     self.prediction_frame['High-Low'] =  self.prediction_frame.High -  self.prediction_frame.Low
     self.prediction_frame =  self.prediction_frame.dropna()
     X =  self.prediction_frame[['Open-Close', 'High-Low']]
     Y = np.where(self.prediction_frame['Close'].shift(-1) >  self.prediction_frame['Close'], 1, -1)
     print("the")
     print(X)
     print(Y)
     return (X, Y)

    def create_regression_trading_condition(self):
        self.prediction_frame['Open-Close'] = self.prediction_frame.Open - self.prediction_frame.Close
        self.prediction_frame['High-Low'] = self.prediction_frame.High - self.prediction_frame.Low
        self.prediction_frame = self.prediction_frame.dropna()
        X = self.prediction_frame[['Open-Close', 'High-Low']]
        Y = self.prediction_frame['Close'].shift(-1) - self.prediction_frame['Close']
        return (X, Y)




