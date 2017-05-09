import pandas as pd

def compute_ratios(sub, num):
    for adsh in sub['adsh']:
        figures = num[num['adsh']==adsh]
        assets = figures[figures['tag']=='Assets']
        liabilities = figures[figures['tag']=='Liabilities']
        assets = assets.reset_index()
        liabilities = liabilities.reset_index()
        liquidity = pd.DataFrame(data=assets, copy=True)
        liquidity['tag'] = 'Liquidity'
        liquidity['value'] = assets['value']/liabilities['value']
        return assets, liabilities, liquidity
        break