
# for docu see danpaquin on github

import gdax
import pprint


public_client = gdax.PublicClient()
actual = public_client.get_product_order_book('BTC-USD', level=1)

pprint.pprint(actual)
