


# pip install -q yahoo_fin
# !mkdir -p data results logs
# ! cp ~/Google\ Drive/My\ Drive/colab/results/* ./results/

# ^c-e send line ^C-r send regiion
import os
import sys

path="/Users/ahsank/save"
os.chdir(path)

path = os.path.expanduser('~/src/ahsank/runml')
print(path)
if not path in sys.path:
  sys.path.append(path)

from runml import pipeline,findata

# switch to branch testv2.01
from importlib import reload
reload(findata)
reload(pipeline)


findata.EPOCHS=200
model = "etf-5b-test"
tickers = ['ARKF', 'ARKK', 'ARKW', 'DAPP', 'DIA', 'DTEC', 'EEM', 'FPX',
            'ICLN', 'IJR', 'IPO', 'IXC', 'IXN', 'IXP', 'IWM', 'IWO', 'IYZ',
            'JETS', 'MGK', 'MGV', 'MTUM',
            'ONLN', 'QQQ', 'SMH', 'SMOG', 'SPY', 'TDIV',
            'VNQ', 'VT', 'VTI', 'VUG', 'WDIV', 'XITK',
            'XLB', 'XLC', 'XLE', 'XLF', 'XLI', 'XLK', 'XLP',
            'XLRE', 'XLU', 'XLV', 'XLY', 'XME', 'XNTK', 'XSW' ]

model = "cry-5a-test"
tickers = [ 'ADA-USD', 'AVAX-USD', 'BTC-USD', 'BCH-USD', 'DOGE-USD', 'DOT-USD',
            'ETH-USD', 'FIL-USD', 'ICP-USD', 'LINK-USD', 'LTC-USD',
            'MATIC-USD', 'SOL-USD', 'TON-USD', 'TRX-USD', 'XRP-USD']

pipeline.IS_VERBOSE = False
mod = pipeline.RateReturnOnly(
    pipeline.FeatureSeq([pipeline.AddDayMonth(),
                         pipeline.AddVWap(),
                         pipeline.AddMA(200),
                         pipeline.Adj()
                         ]))

df, result  = pipeline.runModelCombined(tickers, model, mod, False)

df = pipeline.runModelCombinedVola(tickers, model, mod, False)
df

spyr = result['SPY']
df[df.Ticker=='SPY']
print(spyr.model.metrics_names)

