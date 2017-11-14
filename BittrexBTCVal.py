import json
from bittrex.bittrex import Bittrex
import pprint

bit = Bittrex(None, None)
actual = bit.get_orderbook('USDT-BTC', depth=10)
buys = actual['result']['buy']
sell = actual['result']['sell']
actual['result']['buy'] = buys[0:10]
actual['result']['sell'] = sell[0:10]

pprint.pprint(actual)
