from python_bitvavo_api.bitvavo import Bitvavo
import pprint
import matplotlib.pyplot as plt
import itertools

pp = pprint.PrettyPrinter(indent=2)
bitvavo = Bitvavo()
response = bitvavo.book('NANO-EUR', {"depth": 40})
for item in response['bids']:
  print('Bid:', item)
print("---------------------------------------------------------------------------------")
for item in response['asks']:
  print('Ask:', item)
  
prices = []
bids = []
for item in response['asks']:
    prices.append(float(item[0]))
    bids.append(float(item[1]))
lists = sorted(zip(*[prices, bids]))
prices, bids = list(zip(*lists))

plt.plot(prices, bids)

prices = []
bids = []
for item in response['bids']:
    prices.append(float(item[0]))
    bids.append(float(item[1]))

lists = sorted(zip(*[prices, bids]))
prices, bids = list(zip(*lists))

plt.plot(prices, bids)
plt.show()

highest_bid = float(response["bids"][0][0])
lowest_ask = float(response["asks"][0][0])
print("Spread: " + str(round(((1 - highest_bid/lowest_ask) * 100), 3)) + "%")