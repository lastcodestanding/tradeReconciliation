import pandas as pd
import numpy as np

def convert_currency(df):
    from forex_python.converter import CurrencyRates
    import datetime

    for i in range(len(df)):
        df.iloc[i]['Value'] = (CurrencyRates().get_rate('USD',df.iloc[i]['Currency'], df.iloc[i].date)

    return df

# df sent, df received parameters
def valuationGen(sent, received):

    #Assumption that currency is listed but value of trade is is given in USD.
    #If needed, convert_currency function may be used.

    """The following section is the same in both functions"""
    sent.sort_values(by = params, inplace = True)
    received.sort_values(by = params, inplace = True)

    sent = sent[params].dropna()
    received = received[params].dropna()

    sent['sr'] = np.ones(len(sent))
    received['sr'] = np.zeros(len(received))

    all = pd.concat([sent,received])
    """this previous secion is the same in both functions"""

    #dropping duplicate columns based on the list of parameters defined
    all.drop_duplicates()#O(n) complexity.

    #This leaves all the trades which were different.
    #This dataframe could be used to drill down on trades to understand where
    #errors really are.

    all.groupby(by='sr').sum()

    #Returning the total error from each side (bank and govt.)
    return [all.iloc[0]['value'], all.iloc[1]['value']]


    #time complexity would be O(nlog(n)) due to sorting.
    #Approximately 2e6 trades processed per second assuming 1e8 computations per
    #second.
