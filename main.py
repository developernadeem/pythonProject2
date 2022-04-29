"""
main.py, ADS1 assignment2
created: 27 Apr, 2022
main.py is mainly intended for interactive plots and analysis of data set climate change from world bank
[https://data.worldbank.org/topic/climate-change]
"""
import matplotlib.pyplot as plt
import pandas as pd


def get_indicators_countries():
    """
        This method provides the list of indicators to be studies and countries under observation
    :return: countries, indicators
    """
    # EG.ELC.ACCS.ZS -> Access to electricity (% of population)
    # EG.USE.ELEC.KH.PC -> Electric power consumption (kWh per capita)
    # EG.USE.PCAP.KG.OE -> Energy use (kg of oil equivalent per capita)
    # EN.ATM.CO2E.KT -> CO2 emissions (kt)
    indicators = ['EG.ELC.ACCS.ZS', 'EG.USE.ELEC.KH.PC', 'EG.USE.PCAP.KG.OE', 'EN.ATM.CO2E.KT']
    # this study focus only Pakistan, Great Britain and China
    countries = ['PAK', 'GBR', 'USA']
    return countries, indicators


def read_data(file_name):
    """
        Reads a cvs file and reads a dataframe in World-
        bank format and returns two dataframes: one with years as columns and one with
        countries as columns.
        :param file_name: str
            is name of cvs file to be read for analysis
        """
    df_wb = pd.read_csv(file_name).set_index('Country Name')

    countries, indicators = get_indicators_countries()
    df_wb = df_wb[df_wb['Country Code'].isin(countries) & df_wb['Indicator Code'].isin(indicators)]
    # preprocess data
    df_wb.dropna(axis=1, inplace=True)
    df_wb.reset_index(drop=True, inplace=True)

    df_transpose = df_wb.transpose()

    return df_wb, df_transpose


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read the csv file
    df_world_bank, df_wb_transposed = read_data('API_19_DS2_en_csv_v2_4028487.csv')

    print(df_world_bank.describe())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
