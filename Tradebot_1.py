from Main.Data_Fetch.Data import Data
from Main.Settings import *
from Main.GUI.GUI import Chart

#---------------- Technical Analysis --------
from Technical_Anlaysis.Grouped_Return import Grouped_Return

# _______________ Indicators import __________________
from Technical_Anlaysis.Technical_Indicator.Support_Resistance import Support_Resistance
from Technical_Anlaysis.Technical_Indicator.SMA import SMA
from Technical_Anlaysis.Technical_Indicator.Moving_Averages import MACD
from Technical_Anlaysis.Technical_Indicator.APO import APO
from Technical_Anlaysis.Technical_Indicator.BBANDS import BBANDS
from Technical_Anlaysis.Technical_Indicator.EMA import EMA
from Technical_Anlaysis.Technical_Indicator.MOM import MOMENTUM
from Technical_Anlaysis.Technical_Indicator.RSI import RSI
from Technical_Anlaysis.Technical_Indicator.STDDEV import STDDEV
from Technical_Anlaysis.Market_Prediction.test import test




import pandas as pd

class Tradebot:
    def __init__(self):
        self.data_frame = Data(company_name, start_date, end_date)
        self.data_frame.show_full()
        self.chart = Chart(self.data_frame)



    def Technical_Analysis_calc(self): # APO and the MOM same output

        if support_resistance_TF is True:
            Support_Resistance(100, self.data_frame)


        if SMA_TF is True:
            SMA(self.data_frame)

        if APO_TF is True:
            moving_average = MACD(self.data_frame)
            APO(self.data_frame, moving_average)

        if BBANDS_TF is True:
            BBANDS(self.data_frame)

        if EMA_TF is True:
            EMA(self.data_frame)

        if MOM_TF is True:
            MOMENTUM(self.data_frame)

        if RSI_TF is True:
            RSI(self.data_frame)

        if STDDEV_TF is True:
            STDDEV(self.data_frame)

        if Grouped_Return_TF is True:
            Grouped_Return(self.data_frame)


        if MACD_TF is True or MACD_Histogram_TF is True or MA_10_TF is True or MA_40_TF is True:
            moving_average = MACD(self.data_frame)
            if MACD_TF is True:
                moving_average.macd_calculate()
            if MACD_Histogram_TF is True:
                moving_average.macd_histo_calculate()
            if MA_10_TF is True:
                moving_average.ma_10_calculate()
            if MA_40_TF is True:
                moving_average.ma_40_calculate()


        if Direction_Prediction_TF is True:
            example = test(self.data_frame)
            example.create_classification_trading_condition()





        print("576")

        print(self.data_frame.get_full())

    def candlestick_figure(self):
        self.Technical_Analysis_calc()
        self.chart.show_figure_candlesticks()

    def line_figure(self):
        self.chart.show_figure_line()


    def data_frame_output(self):
        self.data_frame.show_full()


bot = Tradebot()

bot.candlestick_figure()
print("Final Print")
bot.data_frame_output()

