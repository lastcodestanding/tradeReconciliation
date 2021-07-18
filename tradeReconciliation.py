"""
Trade type
TradeID AssetClass Jurisdiction CustomerID Party1 Party2 Value Currency Type

Correctness check based on ID, AssetClass
Summary report 1 - x mismatches, y matches.

Valuation check based on value and currency
Summary report 2 - mismatched value

"""

import pandas as pd
import numpy as np
from correcnessGen import correctnessGen
from valuationGen import valuationGen

#2 dfs built - one for data sent by bank and one for received trades from govt.

sent = pd.read_excel('SentData.csv')
received = pd.read_excel('ReceivedData.csv')

a = correctnessGen(sent,received,['TradeID','AssetClass'])
b = valuationGen(sent, received)

print(f"{a[0]} trades sent by bank were not acknowledged.\n{a[1]} extra trades were sent by the govt.")
print(f"{b[0]} was the value of trades sent by the back that were not acknowledged.\n{b[1]} was the total value of extra trades sent by govt.")
