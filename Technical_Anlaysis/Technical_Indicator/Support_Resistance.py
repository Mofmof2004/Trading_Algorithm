import numpy as np
import pandas as pd





class Support_Resistance():
    in_support = 0
    in_resistance = 0
    def __init__(self, bin_width, data_frame):
        self.bin_width = bin_width
        self.data_frame = data_frame
        self.data_frame_unpacked = data_frame.get_full()
        self.calculate()


    def calculate(self):

        if 'sup_tolerance' not in self.data_frame_unpacked and 'res_tolerance' not in self.data_frame_unpacked and \
                'sup_count' not in self.data_frame_unpacked and 'res_count' not in self.data_frame_unpacked and \
                'sup' not in self.data_frame_unpacked and 'res' not in self.data_frame_unpacked:
            # Creating the self.data_frame_unpacked frame information table
            self.data_frame_unpacked['sup_tolerance'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
            self.data_frame_unpacked['res_tolerance'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
            self.data_frame_unpacked['sup_count'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
            self.data_frame_unpacked['res_count'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
            self.data_frame_unpacked['sup'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))
            self.data_frame_unpacked['res'] = pd.Series(np.zeros(len(self.data_frame_unpacked)))

        for x in range((self.bin_width - 1) + self.bin_width, len(self.data_frame_unpacked)):
            # part of self.data_frame_unpacked being analysed
            data_section = self.data_frame_unpacked[x - self.bin_width:x + 1]

            # Finding support level where in self.data_frame_unpacked section there is the minimal value
            support_level = min(data_section['price'])
            resistance_level = max(data_section['price'])
            # print("Support level: " + str(support_level))
            # print("Resistance level: " + str(resistance_level))
            range_level = resistance_level - support_level
            self.data_frame_unpacked['res'][x] = resistance_level
            self.data_frame_unpacked['sup'][x] = support_level

            # 0.2 = 20%
            # level range area
            self.data_frame_unpacked['sup_tolerance'][x] = support_level + 0.2 * range_level
            self.data_frame_unpacked['res_tolerance'][x] = resistance_level - 0.2 * range_level
            # if price is in the resistance range
            if self.data_frame_unpacked['price'][x] >= self.data_frame_unpacked['res_tolerance'][x] and \
                    self.data_frame_unpacked['price'][x] <= self.data_frame_unpacked['res'][x]:
                self.in_resistance += 1
                self.data_frame_unpacked['res_count'][x] = self.in_resistance

            elif self.data_frame_unpacked['price'][x] <= self.data_frame_unpacked['sup_tolerance'][x] and \
                    self.data_frame_unpacked['price'][x] >= self.data_frame_unpacked['sup'][x]:
                self.in_support += 1
                self.data_frame_unpacked['sup_count'][x] = self.in_support
            else:
                self.in_support = 0
                self.in_resistance = 0


    def signal(self, in_resistance, in_support, x):
        # If two times reach resistance level buy
        if in_resistance > 2:
            self.data_frame_unpacked['signal'][x] = 1
        # If two times reach support level sell
        elif in_support > 2:
            self.data_frame_unpacked['signal'][x] = 0

        else:
            # Npt sure of its use
            self.data_frame_unpacked['signal'][x] = self.data_frame_unpacked['signal'][x - 1]
            self.data_frame_unpacked['positions'] = self.data_frame_unpacked['signal'].diff()
