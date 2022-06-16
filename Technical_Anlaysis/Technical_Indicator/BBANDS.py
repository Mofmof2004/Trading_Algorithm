import statistics as stats
import math as math
from Technical_Anlaysis.Technical_Indicator.SMA import SMA
from Technical_Anlaysis.Technical_Indicator.STDDEV import STDDEV
from Main.Settings import *
import pandas as pd
import numpy as np
class BBANDS:
    '''
    The Bollinger Band (BBANDS) study created
     by John Bollinger plots upper and lower envelope bands around the
     price of the instrument. The width of the bands is based on the
     standard deviation of the closing prices from a moving average of
     price.
     Middle
     Band = n-period moving average

    Upper
     Band = Middle Band + ( y * n-period standard deviation)

    Lower Band = Middle Band - ( y *
     n-period standard deviation)

    Where:

    n = number of periods
    y = factor to apply to the standard deviation value, (typical default for y = 2)
    Detailed:

    Calculate the moving average.
     The formula is:
    d = ((P1-MA)^2 + (P2-MA)^2 + ... (Pn-MA)^2)/n

    Pn is the price you pay for the nth interval
    n is the number of periods you select
    Subtract the moving average
     from each of the individual data points used in the moving average
     calculation. This gives you a list of deviations from the average.
     Square each deviation and add them all together. Divide this sum
     by the number of periods you selected.

    Take the square root of d. This gives you the standard deviation.

    delta = sqrt(d)

    Compute the bands by using the following formulas:
    Upper Band = MA + delta
    Middle Band = MA
    Lower Band = MA - delta

     '''

    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()
        self.calculate()

    def calculate(self):
        close = self.data_frame_unpacked['Close']


        stdev_factor = 2  # Standard Deviation Scaling factor for the upper and lower bands
        sma_class = SMA(self.data_frame)
        sma_values = sma_class.get_sma_output() # moving average of prices for visualization purposes

        upper_band = []  # upper band values
        lower_band = []  # lower band values
        stdev_list = STDDEV(self.data_frame)

        for i in range(len(close)):

            upper_band.append(sma_values[i] + stdev_factor * stdev_list.get_list()[i])
            lower_band.append(sma_values[i] - stdev_factor * stdev_list.get_list()[i])


        self.data_frame_unpacked['MBAND-SMA-' + str(sma_time_period)] = pd.Series(np.zeros(len(self.data_frame_unpacked))) # MiddleBollingerBand20DaySMA
        self.data_frame_unpacked['UBAND-SMA-' + str(sma_time_period)] = pd.Series(np.zeros(len(self.data_frame_unpacked))) # UpperBollingerBand20DaySMA
        self.data_frame_unpacked['LBAND-SMA-' + str(sma_time_period)] = pd.Series(np.zeros(len(self.data_frame_unpacked))) # LowerBollingerBand20DaySMA

        for i in range(len(self.data_frame_unpacked)):
            self.data_frame_unpacked['MBAND-SMA-' + str(sma_time_period)][i] = sma_values[i]
            self.data_frame_unpacked['UBAND-SMA-' + str(sma_time_period)][i] = upper_band[i]
            self.data_frame_unpacked['LBAND-SMA-' + str(sma_time_period)][i] = lower_band[i]


