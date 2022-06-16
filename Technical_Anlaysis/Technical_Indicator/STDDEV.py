
import math as math
from Technical_Anlaysis.Technical_Indicator.SMA import SMA
import pandas as pd
import numpy as np
from Main.Settings import *


class STDDEV:
    '''
    Standard Deviation is a statistical calculation
     used to measure the variability. In trading this value is known
     as volatility. A low standard deviation indicates that the data
     points tend to be very close to the mean, whereas high standard
     deviation indicates that the data points are spread out over a large
     range of values.

    n = number of periods

    Calculate the moving average.
     The formula is:
    d = ((P1-MA)^2 + (P2-MA)^2 + ... (Pn-MA)^2)/n

    Pn is the price you pay for the nth interval
    n is the number of periods you select

    Take the square root of d. This gives you the standard deviation.

    stddev = sqrt(d)

     '''
    stddev_values = [] # history of computed stdev values
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()

        self.calculate()

    def calculate(self):

        time_period = 20  # look back period
        history = []  # history of prices
        sma_class = SMA(self.data_frame)
        sma_values = sma_class.get_sma_output()  # moving average of prices for visualization purposes

        i = 0
        for close_price in self.data_frame_unpacked['Close']:
            history.append(close_price)
            if len(history) > time_period:  # we track at most 'time_period' number of prices
                del (history[0])

            variance = 0  # variance is square of standard deviation
            for hist_price in history:
                variance = variance + ((hist_price - sma_values[i]) ** 2)

            stdev = math.sqrt(variance / len(history))

            self.stddev_values.append(stdev)
            i += 1

        self.data_frame_unpacked['STDDEV-' + str(stddev_time_period)] = pd.Series(
            np.zeros(len(self.data_frame_unpacked)))  # LowerBollingerBand20DaySMA

        for i in range(len(self.data_frame_unpacked)):
            self.data_frame_unpacked['STDDEV-' + str(stddev_time_period)][i] = self.stddev_values[i]

    def get_list(self):
        return self.stddev_values



