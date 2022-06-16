import pandas as pd
import numpy as np

class MACD:
    '''
     The Moving Average Convergence Divergence
      (MACD) was developed by Gerald Appel, and is based on the differences
      between two moving averages of different lengths, a Fast and a Slow moving
      average. A second line, called the Signal line is plotted as a moving
      average of the MACD. A third line, called the MACD Histogram is
      optionally plotted as a histogram of the difference between the
      MACD and the Signal Line.

      MACD = FastMA - SlowMA

     Where:

     FastMA is the shorter moving average and SlowMA is the longer moving average.
     SignalLine = MovAvg (MACD)
     MACD Histogram = MACD - SignalLine
      '''
    
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()
        self.MA_10_values = None
        self.MA_40_values = None
        self.macd_values = None
        self.macd_histogram_values = None

        self.overall_calculate()

    def overall_calculate(self):
        close = self.data_frame_unpacked['Close']
        num_periods_fast = 10  # fast EMA time period
        K_fast = 2 / (num_periods_fast + 1)  # fast EMA smoothing factor
        MA_10 = 0
        num_periods_slow = 40  # slow EMA time period
        K_slow = 2 / (num_periods_slow + 1)  # slow EMA smoothing factor
        MA_40 = 0
        num_periods_macd = 20  # MACD EMA time period
        K_macd = 2 / (num_periods_macd + 1)  # MACD EMA smoothing factor
        ema_macd = 0

        self.MA_10_values = []  # track fast EMA values for visualization purposes
        self.MA_40_values = []  # track slow EMA values for visualization purposes
        self.macd_values = []  # track MACD values for visualization purposes
        self.macd_signal_values = []  # MACD EMA values tracker
        self.macd_histogram_values = []  # MACD - MACD-EMA
        for close_price in close:
            if (MA_10 == 0):  # first observation
                MA_10 = close_price
                MA_40 = close_price
            else:
                MA_10 = (close_price - MA_10) * K_fast + MA_10
                MA_40 = (close_price - MA_40) * K_slow + MA_40

            self.MA_10_values.append(MA_10)
            self.MA_40_values.append(MA_40)

            macd = MA_10 - MA_40  # MACD is fast_MA - slow_EMA
            if ema_macd == 0:
                ema_macd = macd
            else:
                ema_macd = (macd - ema_macd) * K_slow + ema_macd  # signal is EMA of MACD values

            self.macd_values.append(macd)
            self.macd_signal_values.append(ema_macd)
            self.macd_histogram_values.append(macd - ema_macd)


        # self.data_frame = self.data_frame.assign(ClosePrice=pd.Series(close, index=self.data_frame.index))
        # self.data_frame = self.data_frame.assign(FastExponential10DayMovingAverage=pd.Series(MA_10_values, index=self.data_frame.index))
        # self.data_frame = self.data_frame.assign(SlowExponential40DayMovingAverage=pd.Series(MA_40_values, index=self.data_frame.index))
        # self.data_frame = self.data_frame.assign(MovingAverageConvergenceDivergence=pd.Series(macd_values, index=self.data_frame.index))
        # self.data_frame = self.data_frame.assign(MACDHistorgram=pd.Series(macd_historgram_values, index=self.data_frame.index))


    def ma_10_calculate(self):
        self.data_frame_unpacked['MA-10'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
        for i in range(len(self.data_frame_unpacked)):
            self.data_frame_unpacked['MA-10'][i] = self.MA_10_values[i]

    def ma_40_calculate(self):
        self.data_frame_unpacked['MA-40'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
        for i in range(len(self.data_frame_unpacked)):
            self.data_frame_unpacked['MA-40'][i] = self.MA_40_values[i]

    def macd_calculate(self):
        self.data_frame_unpacked['MACD'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
        for i in range(len(self.data_frame_unpacked)):
            self.data_frame_unpacked['MACD'][i] = self.macd_values[i]
    def macd_histo_calculate(self):
        self.data_frame_unpacked['MACD-HISTO'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
        print(self.macd_histogram_values)
        for i in range(len(self.data_frame_unpacked)):
            self.data_frame_unpacked['MACD-HISTO'][i] = self.macd_histogram_values[i]

    def ma_10_values_list(self):
        return self.MA_10_values

    def ma_40_values_list(self):
        return self.MA_40_values







