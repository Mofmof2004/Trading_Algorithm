import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data
class Grouped_Return:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()
        self.Monthly_Return()

    def Monthly_Return(self):


        goog_monthly_return = self.data_frame_unpacked['Adj Close'].pct_change().groupby(
            [self.data_frame_unpacked['Adj Close'].index.year,
             self.data_frame_unpacked['Adj Close'].index.month]).mean()
        goog_montly_return_list = []
        for i in range(len(goog_monthly_return)):
            goog_montly_return_list.append \
                ({'month': goog_monthly_return.index[i][1],
                  'monthly_return': goog_monthly_return.values[i]})
        goog_monthly_return_list = pd.DataFrame(goog_montly_return_list,
                                               columns=('month', 'monthly_return'))

        goog_monthly_return_list.boxplot(column='monthly_return',
                                        by='month')





