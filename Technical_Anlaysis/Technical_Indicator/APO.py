import pandas as pd
import numpy as np


class APO:
    '''
    The Absolute Price Oscillator (APO) is based
     on the absolute differences between two moving averages of different
     lengths, a ‘Fast’ and a ‘Slow’ moving average.

    APO = Fast Exponential Moving Average - Slow Exponential Moving Average
    '''
    def __init__(self, data_frame, moving_averages):
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()
        self.ma = moving_averages
        self.calculate()

    def calculate(self):

        apo_values = []  # track computed absolute price oscillator values
        ma_10_values = self.ma.ma_10_values_list()
        ma_40_values = self.ma.ma_40_values_list()


        self.data_frame_unpacked['APO'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
        for i in range(len(self.data_frame_unpacked)):
            apo_values.append(ma_10_values[i] - ma_40_values[i])
            self.data_frame_unpacked['APO'][i] = apo_values[i]
