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

# (ver)kaufen automatisieren
# Stonks kaufen: x (zwischen 1 und 10 Stufen) nach oben und nach unten (vielleicht auch variieren, also unten und oben unterschiedlich viele)
# Verlauf der letzten z.B. 10 Tage verwenden, um Factor für Differenz zwischen 24h Durchschnittspreis und Stack-Buys zu finden
# https://www.cryptodatadownload.com/data/ alle exchanges (vielleicht auch nur Binance) crawlen, dann auf allen Coins Algorithmus anwenden mit Random Werten für 1. Factor, 2. Differenz, 3. Anzahl Stack Buys
# Neues private Rep machen
# Vielleicht auch Wert auswerten, wie "stabil" ein Algorithmus ist -> Abstand zwischen Wochengewinnen Zusammenrechnen und mit diesem Abstand und Gesamtgewinn einen Wert ausrechnen, der zeigt, ob ein Gewinn wahrscheinlicher ist, als bei anderen. Damit verhindert man, dass seltene Einzelevents, bei denen der Wert skyrocketet die Auswertung verfälschen, da diese Events seltener passieren.