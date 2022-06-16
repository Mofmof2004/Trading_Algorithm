
# loading the class self.data_frame from the package pandas_datareader
from pandas_datareader import data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Data fetch == data format
class Data():
    # loading the class self.data_frame from the package pandas_datareader
    from pandas_datareader import data
    chart_data = None
    data_frame = None

    def __init__(self, stock_name, start_data, end_date, source='yahoo'):
        self.source = source
        self.start_date = start_data
        self.stock_name = stock_name
        self.end_date = end_date

        self.date_check()

        self.fetch()
        self.frame_constructor()



    def fetch(self):
        # try to fetch self.data_frame and store it
        try:
            self.chart_data = self.data.DataReader(self.stock_name, self.source, self.start_date, self.end_date)

        except KeyError:
            # check if name is right
            self.stock_name_error()

        self.SRC_DATA_FILENAME = (self.stock_name).upper() + '_data.pkl'
        self.chart_data.to_pickle(self.SRC_DATA_FILENAME)

        # Call the function DataReader from the class self.data_frame
        pd.set_option('display.max_rows', 1000)
        pd.set_option('display.max_columns', 1500)
        pd.set_option('display.width', 1000)
        self.chart_data = self.data.DataReader(self.stock_name, self.source, self.start_date, self.end_date)

    def date_check(self):
        import re
        # Checks the dates entered are in the right format
        format = '[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]+'
        match_start_date = bool(re.match(format, self.start_date))
        match_end_date = bool(re.match(format, self.end_date))
        # If not make user renter

        while match_start_date is not True:
            new_date = input("ERROR: SYNTAX ERROR \nPLEASE ENTER A VALID START DATE \nFORMAT: 0000-00-00\nENTER: ")
            self.start_date = new_date
            match_start_date = bool(re.match(format, self.start_date))

        while match_end_date is not True:
            new_date = input("ERROR: SYNTAX ERROR \nPLEASE ENTER A VALID END DATE \nFORMAT: 0000-00-00\nENTER: ")
            self.end_date = new_date
            match_end_date = bool(re.match(format, self.end_date))

    def stock_name_error(self):
        try:
            print("ERROR: SYNTAX ERROR")
            self.stock_name = input("PLEASE ENTER A VALID STOCK NAME \nENTER: ")
            self.chart_data = self.data.DataReader(self.stock_name, self.source, self.start_date, self.end_date)
        except KeyError:
            self.stock_name_error()


    def frame_constructor(self):
        # self.data_frame = pd.DataFrame(index=self.chart_data.index)
        self.data_frame = self.chart_data
        self.data_frame['price'] = self.chart_data['Adj Close']
        self.data_frame['positions'] = pd.Series(np.zeros(len(self.data_frame)))
        self.data_frame['signal'] = pd.Series(np.zeros(len(self.data_frame)))

    def update(self, new_frame):
        print(self.data_frame)
        # self.data_frame = new_frame
        print(7767)
        print(self.data_frame)

    def show_basic(self):
        print(self.chart_data)

    def show_full(self):
        print(self.data_frame)

    def get_basic(self):
        return self.chart_data

    def get_full(self):
        return self.data_frame

