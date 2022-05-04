"""
main.py, ADS1 assignment2
created: 27 Apr, 2022
main.py is mainly intended for interactive plots and analysis of data set climate change from world bank
[https://data.worldbank.org/topic/climate-change]
"""
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr
import numpy as np


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
    # this study focus only Pakistan, Great Britain and United states
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
    df_wb = pd.read_csv(file_name)

    countries, indicators = get_indicators_countries()
    df_wb = df_wb[df_wb['Country Code'].isin(countries) & df_wb['Indicator Code'].isin(indicators)]
    # preprocess data
    # df_wb.dropna(axis=1, inplace=True)
    # reset index and drop the old ones
    df_wb.reset_index(drop=True, inplace=True)
    # drop the two columns to make selection a simple process in transposed data
    df_wb.drop(df_wb.columns[[0, 2]], axis=1, inplace=True)
    df_transpose = df_wb.transpose()
    # Set multilevel column indexes
    df_transpose.columns = pd.MultiIndex.from_arrays(df_transpose.iloc[0:2].values)
    df_transpose = df_transpose.iloc[2:]
    print(df_transpose.head())
    return df_wb, df_transpose


def generate_graph(df, title, x_label, y_label, legend):
    """
        Plots timeline series in given data
        :param df: DataFrame
            Sorted dataframe which need to be plotted
        :param title: str
        :param x_label: str
        :param y_label: str
        :param legend: list
            list of legend corresponding to df
        """
    df.plot(style=["r-", "g:", "b--"], title=title, xlabel=x_label, ylabel=y_label)
    plt.xticks(rotation=70)
    plt.legend(legend)
    plt.savefig(title + ".png")
    plt.show()


def calculate_correlation(x, y, title):
    """
    calculate the pearsonr corr between to variables
    :param title:
    :param x: numpy array
    :param y:numpy array
    """
    r, p = pearsonr(x, y)
    print(title)
    print("correlation coefficient r:", r)
    print("probability p:", p)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read the csv file
    df_world_bank, df_wb_transposed = read_data('API_19_DS2_en_csv_v2_4028487.csv')

    generate_graph(
        df_wb_transposed[[("PAK", "EG.USE.ELEC.KH.PC"), ("GBR", "EG.USE.ELEC.KH.PC"), ("USA", "EG.USE.ELEC.KH.PC")]],
        "Electric power consumption in PAK, GBR and USA",
        "Electric power",
        "kWh per capita", ["PAK", "GBR", "USA"])

    generate_graph(df_wb_transposed[[("PAK", "EN.ATM.CO2E.KT"), ("GBR", "EN.ATM.CO2E.KT"), ("USA", "EN.ATM.CO2E.KT")]],
                   "CO2 emission in PAK, GBR and USA", "CO2 emission", "kt", ["PAK", "GBR", "USA"])

    generate_graph(df_wb_transposed[[("PAK", "EG.ELC.ACCS.ZS"), ("GBR", "EG.ELC.ACCS.ZS"), ("USA", "EG.ELC.ACCS.ZS")]],
                   "Access to electricity in PAK, GBR and USA", "Access to electricity", "% of population",
                   ["PAK", "GBR", "USA"])

    generate_graph(
        df_wb_transposed[[("PAK", "EG.USE.PCAP.KG.OE"), ("GBR", "EG.USE.PCAP.KG.OE"), ("USA", "EG.USE.PCAP.KG.OE")]],
        "Energy use in PAK, GBR and USA", "Energy use", "kg of oil per capita",
        ["PAK", "GBR", "USA"])
    #   find correlation between variables
    df_wb_transposed.dropna(inplace=True)
    electric = df_wb_transposed[[("PAK", "EG.ELC.ACCS.ZS")]].to_numpy().flatten()
    co2_emission = df_wb_transposed[[("PAK", "EN.ATM.CO2E.KT")]].to_numpy().flatten()
    # find corr between access to electricity and CO2 emission
    calculate_correlation(electric, co2_emission, "electricity vs CO2 emission")
    # Electric power consumption and CO2 emission
    electric_usage = df_wb_transposed[[("PAK", "EG.USE.ELEC.KH.PC")]].to_numpy().flatten()
    # find corr between access to Electric power consumption and CO2 emission
    calculate_correlation(electric_usage, co2_emission, "Electric power consumption vs CO2 emission")
    # Energy use vs CO2 emission
    oil_energy = df_wb_transposed[[("PAK", "EG.USE.PCAP.KG.OE")]].to_numpy().flatten()
    # find corr between access to Energy use and CO2 emission
    calculate_correlation(oil_energy, co2_emission, "Energy use vs CO2 emission")
    # plot the corr graph
    plt.figure()
    plt.plot(electric_usage, co2_emission, "x")
    plt.xlabel("electric_usage")
    plt.ylabel("$C0_2$")
    plt.show()
