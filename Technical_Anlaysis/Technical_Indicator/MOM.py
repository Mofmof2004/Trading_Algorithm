import pandas as pd
import numpy as np
from Main.Settings import *

class MOMENTUM:
    '''
    The Momentum (MOM) indicator compares the
     current price with the previous price from a selected number of
     periods ago. This indicator is similar to the “Rate of Change” indicator,
     but the MOM does not normalize the price, so different instruments
     can have different indicator values based on their point values.

     MOM =  Price - Price of n periods ago
     '''
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()
        self.calculate()

    def calculate(self):
        history = []  # history of observed prices to use in momentum calculation
        mom_values = []  # track momentum values for visualization purposes

        for close_price in self.data_frame_unpacked['Close']:
            history.append(close_price)
            if len(history) > mom_time_period:  # history is at most 'time_period' number of observations
                del (history[0])

            mom = close_price - history[0]
            mom_values.append(mom)

        self.data_frame_unpacked['MOM'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
        for i in range(len(self.data_frame_unpacked)):
            self.data_frame_unpacked['MOM'][i] = mom_values[i]
