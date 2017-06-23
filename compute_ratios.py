import os
import pandas as pd

def compute_quarter(sub, num):
    ratios = pd.DataFrame(columns=num.columns)
    for adsh in sub['adsh']:
        figures = num[num['adsh']==adsh]

        assets = figures[figures['tag']=='Assets']
        liabilities = figures[figures['tag']=='Liabilities']
        assets = assets.reset_index()
        liabilities = liabilities.reset_index()

        liquidity = pd.DataFrame(data=assets, copy=True)
        liquidity['tag'] = 'Liquidity'
        liquidity['value'] = assets['value']/liabilities['value']

        ratios = ratios.append(liquidity.reset_index())

    return ratios
