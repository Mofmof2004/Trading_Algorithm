import pandas as pd
import numpy as np
from Main.Settings import *

class EMA:

    '''
    The Exponential Moving Average (EMA) represents
     an average of prices, but places more weight on recent prices. The
     weighting applied to the most recent price depends on the selected
     period of the moving average. The shorter the period for the EMA,
     the more weight that will be applied to the most recent price.

    EMA = ( P - EMAp ) * K + EMAp

    Where:

    P = Price for the current period
    EMAp = the Exponential moving Average for the previous period
    K = the smoothing constant, equal to 2 / (n + 1)
    n = the number of periods in a simple moving average roughly approximated by the EMA
    '''

    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()
        self.calculate()

    def calculate(self):

        K = 2 / (num_periods + 1)  # smoothing constant
        ema_p = 0

        ema_values = []  # to hold computed EMA values
        for close_price in self.data_frame_unpacked['Close']:
            if (ema_p == 0):  # first observation, EMA = current-price
                ema_p = close_price
            else:
                ema_p = (close_price - ema_p) * K + ema_p

            ema_values.append(ema_p)

        self.data_frame_unpacked['EMA'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
        for i in range(len(self.data_frame_unpacked)):
            self.data_frame_unpacked['EMA'][i] = ema_values[i]


