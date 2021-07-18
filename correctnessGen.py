import pandas as pd
import numpy as np

# df sent, df received, list of comparison parameters in order.
def correctnessGen(sent, received, params):

    #O(n log(n)) complexity
    sent.sort_values(by = params, inplace = True)
    received.sort_values(by = params, inplace = True)

    sent = sent[params].dropna()
    received = received[params].dropna()

    sent['sr'] = np.ones(len(sent))
    received['sr'] = np.zeros(len(received))

    all = pd.concat([sent,received])

    #dropping duplicate columns based on the list of parameters defined
    all.drop_duplicates(subset=params)#O(n) complexity.

    #keeping only the 'sr' column as that identifies which side caused the error
    #may be grouped by any field if required.
    all = all['sr']

    cnt = all.sum()#represents number of trades sent but not correctly received back.

    #Only returning the final number of errors from each side.
    return [cnt,len(all)-cnt]

    #time complexity would be O(nlog(n)) due to sorting.
    #Approximately 2e6 trades processed per second assuming 1e8 computations per
    #second.
