#!/usr/local/bin/python

# for reverence: github kmadac
import bitstamp.client
import pprint

pp = pprint.PrettyPrinter(indent=4)

bit = bitstamp.client.Public()
actual = bit.order_book()

actual['bids'] = actual['bids'][1:10]
actual['asks'] = actual['asks'][1:10]

pp.pprint(actual)
