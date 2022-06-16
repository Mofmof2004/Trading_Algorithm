import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from Main.Settings import *
import statistics as stats
from Technical_Anlaysis.Technical_Indicator.STDDEV import STDDEV

from Technical_Anlaysis.Technical_Indicator.Support_Resistance import Support_Resistance

class Chart:
    # loading the class self.data_frame from the package pandas_datareader
    from pandas_datareader import data

    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()
        # Creating Subplots
        self.fig = plt.figure()

        # Finding which axis is needed to be created
        axis_2_TF = APO_TF or MACD_TF or MOM_TF or RSI_TF or STDDEV_TF
        axis_3_TF = MACD_Histogram_TF or RSI_TF
        # Number of axis needed to be created
        axis_sum = sum([axis_2_TF, axis_3_TF])+1
        print(axis_sum)

        # Creating all the axis
        self.ax1 = self.fig.add_subplot(axis_sum, 1, 1, ylabel='Google price in $')
        if axis_2_TF is True:

            self.ax2 = self.fig.add_subplot(axis_sum, 1, 2, ylabel='MACD')
        if axis_3_TF is True:
            self.ax3 = self.fig.add_subplot(axis_sum, 1, axis_sum, ylabel='MACD HISTOGRAM')
            # Remove x axis labels
            plt.gca().axes.get_xaxis().set_visible(False)

    def param_update(self, new_data_frame):
        self.data_frame_unpacked = new_data_frame


    def show_figure_candlesticks(self):
        from mpl_finance import candlestick_ohlc
        import matplotlib.dates as mpl_dates

        # Defining a dataframe
        stock_prices = self.data_frame_unpacked
        stock_prices['Date'] = stock_prices.index
        print(stock_prices)
        ohlc = stock_prices.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
        ohlc['Date'] = pd.to_datetime(ohlc['Date'])
        ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
        ohlc = ohlc.astype(float)



        # alpha is the opasity of the candletsticks
        candlestick_ohlc(self.ax1, ohlc.values, width=0.6, colorup='green',
                         colordown='red', alpha=0.9)

        # Setting labels & titles
        self.ax1.set_xlabel('Date')
        self.ax1.set_ylabel('Price')
        # fig.suptitle('Stock Prices of a week')

        # Formatting Date-
        date_format = mpl_dates.DateFormatter('%d-%m-%Y')
        self.ax1.xaxis.set_major_formatter(date_format)
        if support_resistance_TF is True:
            self.support_resistance_plot(view_only=False)

        if SMA_TF is True:
            self.sma_plot()

        if MACD_TF is True:
            self.macd_plot()

        if MA_10_TF is True:
            self.ma_10_plot()

        if MA_40_TF is True:
            self.ma_40_plot()

        if MACD_Histogram_TF is True:
            self.macd_histogram_plot()

        if APO_TF is True:
            self.apo_plot()

        if BBANDS_TF is True:
            self.bbands_plot()

        if EMA_TF is True:
            self.ema_plot()

        if MOM_TF is True:
            self.mom_plot()

        if RSI_TF is True:
            self.rsi_plot()

        if STDDEV_TF is True:
            self.stddev_plot()

        if Grouped_Return_TF:
            self.grouped_return_plot()

        self.fig.autofmt_xdate()
        self.fig.tight_layout()

        plt.show()

    def show_figure_line(self, sup_res=False, sma=False):

        # Graph setting
        self.data_frame_constructor()
        # Creating the frame to plot the values on the graph
        fig = plt.figure()

        # declaring ax1
        self.ax1 = fig.add_subplot(111, ylabel='Price in $')
        # Plotting the prices on the graph
        self.data_frame_unpacked['price'].plot(ax=self.ax1, color='r', lw=2.)

        if sup_res is True:
            view_only = False

            self.support_resistance_plot(view_only=view_only)
        if sma is True:
            self.sma_plot()

        if MACD_Histogram_TF is True:
            self.macd_histogram_plot()

        # Set self.data_frame frame output options
        plt.legend()
        plt.show()

    def support_resistance_plot(self, view_only=True):
        self.data_frame_unpacked['sup'].plot(ax=self.ax1, color='g', lw=2.)
        self.data_frame_unpacked['res'].plot(ax=self.ax1, color='b', lw=2.)

        if view_only is False:
            self.ax1.plot(self.data_frame_unpacked.loc[self.data_frame_unpacked.positions == 1.0].index,
                     self.data_frame_unpacked.price[self.data_frame_unpacked.positions == 1.0],
                     '^', markersize=7, color='k', label='buy')
            self.ax1.plot(self.data_frame_unpacked.loc[self.data_frame_unpacked.positions == -1.0].index,
                     self.data_frame_unpacked.price[self.data_frame_unpacked.positions == -1.0],
                     'v', markersize=7, color='k', label='sell')

    def sma_plot(self):
        self.data_frame_unpacked['SMA-20'].plot(ax=self.ax1, color='g', lw=2., legend=True)

        # self.ax1.plot(self.data_frame.loc[self.data_frame.ClosePrice].index,
        #               self.data_frame.price[self.data_frame.ClosePrice], color='g', lw=2., legend=True)

    def macd_plot(self):
        macd = self.data_frame_unpacked['MACD']
        macd.plot(ax=self.ax2, color='black', lw=2., legend=True)

    def ma_10_plot(self):

        ma_10 = self.data_frame_unpacked['MA-10']
        ma_10.plot(ax=self.ax1, color='b', lw=2., legend=True)

    def ma_40_plot(self):
        ma_40 = self.data_frame_unpacked['MA-40']
        ma_40.plot(ax=self.ax1, color='r', lw=2., legend=True)

    def macd_histogram_plot(self):
        print("yes")
        macd_histogram = self.data_frame_unpacked['MACD-HISTO']
        macd_histogram.plot(ax=self.ax3, color='r', kind='bar', legend=True, use_index=False)

    def apo_plot(self):
        apo = self.data_frame_unpacked['APO']
        apo.plot(ax=self.ax2, color='black', lw=2., legend=True)

    def bbands_plot(self):
        mband = self.data_frame_unpacked['MBAND-SMA-'+str(sma_time_period)]
        uband = self.data_frame_unpacked['UBAND-SMA-'+str(sma_time_period)]
        lband = self.data_frame_unpacked['LBAND-SMA-'+str(sma_time_period)]
        mband.plot(ax=self.ax1, color='b', lw=2., legend=True)
        uband.plot(ax=self.ax1, color='g', lw=2., legend=True)
        lband.plot(ax=self.ax1, color='r', lw=2., legend=True)

    def ema_plot(self):
        ema = self.data_frame_unpacked['EMA']
        ema.plot(ax=self.ax1, color='b', lw=2., legend=True)

    def mom_plot(self):
        mom = self.data_frame_unpacked['MOM']
        mom.plot(ax=self.ax2, color='b', lw=2., legend=True)


    def close_price_plot(self):
        close_price = self.data_frame_unpacked['ClosePrice']
        close_price.plot(ax=self.ax1, color='g', lw=2., legend=True)

    def rsi_plot(self):
        rs_loss = self.data_frame_unpacked['RelativeStrengthAvgLoss-' + str(rsi_time_period)]
        rs_gain = self.data_frame_unpacked['RelativeStrengthAvgGain-' + str(rsi_time_period)]
        rsi = self.data_frame_unpacked['RSI-' + str(rsi_time_period)]
        rs_loss.plot(ax=self.ax2, color='r', lw=2., legend=True)
        rs_gain.plot(ax=self.ax2, color='g', lw=2., legend=True)
        rsi.plot(ax=self.ax3, color='b', lw=2., legend=True)

    def stddev_plot(self):
        stddev =  self.data_frame_unpacked['STDDEV-' + str(stddev_time_period)]
        stddev.plot(ax=self.ax2, color='b', lw=2., legend=True)
        self.ax2.axhline(y=stats.mean(STDDEV(self.data_frame).get_list()), color='k')

    def grouped_return_plot(self):
        ax = plt.gca()
        labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ax.set_xticklabels(labels)
        ax.set_ylabel('GOOG return')
        plt.tick_params(axis='both', which='major', labelsize=7)
        plt.title(company_name + " Monthly return " + start_date + str(" / ") + end_date)
        plt.suptitle("")
        plt.show()

    # ema code not included
    # ema_macd = self.data_frame_unpacked['Exponential20DayMovingAverageOfMACD']
    # ema_macd.plot(ax=ax2, color='g', lw=2., legend=True)




# chart = Chart('TSLA', '2021-03-01', '2021-09-08')

# chart.show_figure_candlesticks(sup_res=True, sma=True)
# chart.show_figure_line()
