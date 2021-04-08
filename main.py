from yahoo_fin import stock_info as si
import tulipy as ti
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import sched, time
from luno_python.client import Client
from datetime import datetime
import os

c = Client(api_key_id='apiid', api_key_secret='apisecret')

#parameters:
s = sched.scheduler(time.time, time.sleep)

def run(sc): 
    try:
        dfser = si.get_data("ETH-BTC")
        dfser = dfser[::-1]
        heiclo = (dfser['close']+dfser['open']+dfser['high']+dfser['low'])/4
        heiclo = heiclo.dropna()
        heiclo = heiclo.reset_index(drop=True)
        heinum = heiclo.values
        heinum = heinum.copy(order='C')
        heinum[np.isnan(heinum)] = .03
        dfser = dfser['adjclose']
        dfser = dfser.dropna()
        dfser = dfser.reset_index(drop=True)
        dfnum = dfser.values
        dfnum = dfnum.copy(order='C')
        dfnum[np.isnan(dfnum)] = .03
        
        MALEB = ti.sma(heinum, period=3)
        MAHEB = ti.sma(heinum, period=7)
        MALEB = MALEB.tolist()
        MAHEB = MAHEB.tolist()
        MADEB = []
        for x in range(100):
            MADEB.insert(x,MALEB[x]-MAHEB[x])
        plt.style.use('dark_background')
        plt.plot(heinum, linewidth=0.7, color='#b0b0b0')
        plt.plot(dfnum, linewidth=1, color='#2629de')
        plt.plot(MALEB, linewidth=0.7, color='#00ff1a')
        plt.plot(MAHEB, linewidth=0.7, color='#ff0000')
        plt.xlabel('Days')
        plt.ylabel('Price in ETH/BTC')
        plt.title('ETH/BTC chart')
        plt.xlim(left=60,right=-4)
        plt.autoscale(enable=True, axis='y', tight=False)
        plt.grid()
        plt.savefig('ETHBTC.png',dpi=500)
        #plt.plot(MAD)
        #plt.show()
        plt.close()


        dfser = si.get_data("BTC-USD")
        dfser = dfser[::-1]
        heiclo = (dfser['close']+dfser['open']+dfser['high']+dfser['low'])/4
        heiclo = heiclo.dropna()
        heiclo = heiclo.reset_index(drop=True)
        heinum = heiclo.values
        heinum = heinum.copy(order='C')
        heinum[np.isnan(heinum)] = .03
        dfser = dfser['adjclose']
        dfser = dfser.dropna()
        dfser = dfser.reset_index(drop=True)
        dfnum = dfser.values
        dfnum = dfnum.copy(order='C')
        dfnum[np.isnan(dfnum)] = .03
        
        MALBU = ti.ema(heinum, period=3)
        MAHBU = ti.sma(heinum, period=7)
        MALBU = MALBU.tolist()
        MAHBU = MAHBU.tolist()
        MADBU = []
        for x in range(100):
            MADBU.insert(x,MALBU[x]-MAHBU[x])
        plt.style.use('dark_background')
        plt.plot(heinum, linewidth=0.7, color='#b0b0b0')
        plt.plot(dfnum, linewidth=1, color='#2629de')
        plt.plot(MALBU, linewidth=0.7, color='#00ff1a')
        plt.plot(MAHBU, linewidth=0.7, color='#ff0000')
        plt.xlabel('Days')
        plt.ylabel('Price in BTC/USD')
        plt.title('BTC/USD chart')
        plt.xlim(left=60,right=-4)
        plt.autoscale(enable=True, axis='y', tight=False)
        plt.grid()
        plt.savefig('BTCUSD.png',dpi=500)
        #plt.plot(MAD)
        #plt.show()
        plt.close()


        dfser = si.get_data("ETH-USD")
        dfser = dfser[::-1]
        heiclo = (dfser['close']+dfser['open']+dfser['high']+dfser['low'])/4
        heiclo = heiclo.dropna()
        heiclo = heiclo.reset_index(drop=True)
        heinum = heiclo.values
        heinum = heinum.copy(order='C')
        heinum[np.isnan(heinum)] = .03
        dfser = dfser['adjclose']
        dfser = dfser.dropna()
        dfser = dfser.reset_index(drop=True)
        dfnum = dfser.values
        dfnum = dfnum.copy(order='C')
        dfnum[np.isnan(dfnum)] = .03
        
        MALEU = ti.ema(heinum, period=3)
        MAHEU = ti.sma(heinum, period=7)
        MALEU = MALEU.tolist()
        MAHEU = MAHEU.tolist()
        MADEU = []
        for x in range(100):
            MADEU.insert(x,MALEU[x]-MAHEU[x])
        plt.style.use('dark_background')
        plt.plot(heinum, linewidth=0.7, color='#b0b0b0')
        plt.plot(dfnum, linewidth=1, color='#2629de')
        plt.plot(MALEU, linewidth=0.7, color='#00ff1a')
        plt.plot(MAHEU, linewidth=0.7, color='#ff0000')
        plt.xlabel('Days')
        plt.ylabel('Price in ETH/USD')
        plt.title('ETH/USD chart')
        plt.xlim(left=60,right=-4)
        plt.autoscale(enable=True, axis='y', tight=False)
        plt.grid()
        plt.savefig('ETHUSD.png',dpi=500)
        #plt.plot(MAD)
        #plt.show()
        plt.close()

        fw = open("State.txt", "w")
        log = open("log.txt", "a")
        log.write("<p>")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S %d/%m/%y")
        fw.write(current_time)
        log.write(current_time)
        balXBT = c.get_balances('XBT')['balance'][1]['balance']
        balETH = c.get_balances('ETH')['balance'][1]['balance']
        balUSD = c.get_balances('USDC')['balance'][0]['balance']
        fw.write("<p>")
        fw.write(balXBT)
        fw.write(" BTC</p><p>")
        fw.write(balETH)
        fw.write(" ETH</p><p>")
        fw.write(balUSD)
        fw.write(" USD</p>")

        closepriceEB = c.list_trades(pair="ETHXBT")
        closepriceBU = c.list_trades(pair="XBTUSDC")
        closepriceEU = c.list_trades(pair="ETHUSDC")
        closepriceEB = closepriceEB['trades'][0]['price']
        closepriceBU = closepriceBU['trades'][0]['price']
        closepriceEU = closepriceEU['trades'][0]['price']

        if (MADEU[0] > 0 and MADEB[0] > 0):
            print("Buying ETH, price is going up!")
            log.write(" Buying ETH, price is going up! ")
            if(float(balXBT)/float(closepriceEB) > 0.01):
                try:
                    c.post_limit_order(pair='ETHXBT', type='BID', volume='0.01', price = closepriceEB)
                    print("Post limit order, buy ETH from BTC at price: ", closepriceEB)
                    log.write(" Post limit order, buy ETH from BTC at price: ")
                    log.write(closepriceEB)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S %d/%m/%y")
                except Exception as e:
                    print(e)
                    log.write(" error: ")
                    log.write(e)

            if(float(balUSD)/float(closepriceEU) > 0.01):
                try:
                    c.post_limit_order(pair='ETHUSDC', type='BID', volume='0.01', price = closepriceEU)
                    print("Post limit order, buy ETH from USDC at price: ", closepriceEU)
                    log.write(" Post limit order, buy ETH from USDC at price: ")
                    log.write(closepriceEU)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S %d/%m/%y")
                except Exception as e:
                    print(e)
                    log.write(" error: ")
                    log.write(e)
        
        if (MADBU[0] > 0 and MADEB[0] < 0):
            print("Buying BTC, price is going up!")
            log.write(" Buying BTC, price is going up! ")
            if(float(balUSD)/float(closepriceBU) > 0.0005):
                try:    
                    c.post_limit_order(pair='USDCXBT', type='BID', volume='0.0005', price = closepricesBU)
                    print("Post limit order, buy BTC from USDC at price: ", closepriceBU)
                    log.write(" Post limit order, buy BTC from USDC at price: ")
                    log.write(closepriceBU)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S %d/%m/%y")
                except Exception as e:
                    print(e)
                    log.write(" error: ")
                    log.write(e)

            if(float(balETH) > 0.01):
                try:
                    c.post_limit_order(pair='ETHXBT', type='ASK', volume='0.01', price = closepricesEB)
                    print("Post limit order, buy BTC from ETH at price: ", closepriceEB)
                    log.write(" Post limit order, buy buy BTC from ETH at price: ")
                    log.write(closepriceEB)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S %d/%m/%y")
                except Exception as e:
                    print(e)
                    log.write(" error: ")
                    log.write(e)
        
        if (MADEU[0] < 0 and MADBU[0] < 0):
            print("Buying USDC, price is going up!")
            log.write(" Buying USDC, price is going up! ")
            if(float(balXBT) > 0.0005):
                try:    
                    c.post_limit_order(pair='XBTUSDC', type='ASK', volume='0.0005', price = closepriceBU)
                    print("Post limit order, buy USDC from BTC at price: ", closepriceBU)
                    log.write(" Post limit order, buy USDC from BTC at price: ")
                    log.write(closepriceBU)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S %d/%m/%y")
                except Exception as e:
                    print(e)
                    log.write(" error: ")
                    log.write(e)

            if(float(balETH) > 0.01):
                try:
                    c.post_limit_order(pair='ETHUSDC', type='ASK', volume='0.01', price = closepriceEU)
                    print("Post limit order, buy USDC from ETH at price: ", closepriceEU)
                    log.write(" Post limit order, buy buy USDC from ETH at price: ")
                    log.write(closepriceEU)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S %d/%m/%y")
                except Exception as e:
                    print(e)
                    log.write(" error: ")
                    log.write(e)

        else:
            print("Do nothing!")
            log.write(" Do nothing! ")
        log.write("</p>")
        fw.close()
        log.write("\n")
        log.close()
    except Exception as e:
        print(e)
    

    s.enter(3600, 1, run, (sc,))
    
s.enter(1, 1, run, (s,))

s.run()
