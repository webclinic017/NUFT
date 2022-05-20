import multiprocessing as mp
import concurrent.futures as cf
import KucoinClass as kc
import binance_websocket_class as bc
import pandas as pd
import queue_fix

coins = ['BTC-USDT', 'ETH-USDT']

    

if __name__ == '__main__':
	with cf.ProcessPoolExecutor() as executor:
		q = mp.Queue()
		kucoinwebsocket = kc.Kucoin_Websocket(q,coins)
		binancewebsoocket = bc.Binance_Websocket(q,coins)
		#executor.submit(kucoinwebsocket.start())
		executor.submit(binancewebsoocket.start())
		#p.start()
