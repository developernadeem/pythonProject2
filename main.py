"""
main.py, ADS1 assignment2
created: 27 Apr, 2022
main.py is mainly intended for interactive plots and analysis of data set climate change from world bank
[https://data.worldbank.org/topic/climate-change]
"""
import matplotlib.pyplot as plt
import pandas as pd


def read_data(file_name):
    """
        Reads a cvs file and reads a dataframe in World-
        bank format and returns two dataframes: one with years as columns and one with
        countries as columns.
        :param file_name: str
            is name of cvs file to be read for analysis
        """
    df_wb = pd.read_csv(file_name)
    df_transpose = df_world_bank.transpose()
    return df_wb, df_transpose


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read the csv file
    df_world_bank, df_wb_transposed = read_data('API_19_DS2_en_csv_v2_4028487.csv')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
