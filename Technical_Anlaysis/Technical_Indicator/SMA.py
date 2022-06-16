import pandas as pd
import numpy as np
from Main.Settings import *

class SMA:
    '''

            The Simple Moving Average (SMA) is calculated
             by adding the price of an instrument over a number of time periods
             and then dividing the sum by the number of time periods. The SMA
             is basically the average price of the given time period, with equal
             weighting given to the price of each period.

            Simple Moving Average
            SMA = ( Sum ( Price, n ) ) / n

            Where: n = Time Period
            '''

    close_price = None
    sma_values = []
    history = [] #to track a history of prices
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()

        self.calculate()

    def calculate(self):
        import statistics as stats
        for close_price in self.data_frame_unpacked['Close']:
            self.history.append(close_price)
            if len(self.history) > sma_time_period:  # we remove oldest price because we only average over last 'time_period' prices
                del (self.history[0])

            self.sma_values.append(stats.mean(self.history))

        # Old version
        # self.data_frame_unpacked = self.data_frame_unpacked.assign(ClosePrice=pd.Series(close, index=self.data_frame_unpacked.index))
        # self.data_frame.get_full = self.data_frame.get_full().assign(Simple20DayMovingAverage=pd.Series(sma_values, index=self.data_frame.get_full.index))

        self.data_frame_unpacked['SMA-20'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
        for i in range(len(self.data_frame_unpacked)):
            self.data_frame_unpacked['SMA-20'][i] = self.sma_values[i]




    def get_sma_output(self):
        return self.sma_values
    def get_history(self):
        return self.history
    def get_close_price_output(self):
        return self.close_price
