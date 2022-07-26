# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 12:18:04 2022

@author: 14015
"""
import time
import requests
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats
import pandas as pd
import statistics

#List tickers

tic = ['ZRX','1INCH','AAVE','GHST','ACA','AKT','ALGO','AIR','ANKR','ANT','ASTR','AUDIO','AVAX','AXS','BADGER','BAL','BNT','BAND','BAT','BICO','BNC','BTC','BCH','FIDA','ADA','CTSI','LINK','CHZ','COMP','ATOM','CQT','CRV','DASH','MANA','DOGE','DYDX','EWT','ENJ','EOS','ETH','ETC','ENS','FIL','FLOW','GALA','GNO','ICX','IMX','INJ','KAR','KAVA','KEEP','KP3R','KILT','KIN','KINT','KSM','KNC','LSK','LTC','LPT','LRC','MKR','MNGO','MC','MINA','MIR','XMR','GLMR','MOVR','ALICE','NANO','OCEAN','OMG','ORCA','OXT','OGN','OXY','PAXG','PERP','PHA','DOT','MATIC','PSTAKE','QTUM','RARI','RAY','REN','XRP','SBR','SRM','SHIB','SDN','SC','SOL','SGB','ATLAS','POLIS','STEP','STORJ','SUSHI','SNX','TBTC','LUNA','UST','XTZ','GRT','SAND','TRX','UNI','WAVES','WOO','WBTC','YFI','YGG','ZEC']


stored = []


####get daily historical close data
def historical_data_close(i):
    
    #interval is in minutes. 1440 is 1 day
    #This gets daily intervals. 
    #can pickup up to 720 intervals?
    endhtml = i+'USD'+'&interval=1440'
    resp = requests.get('https://api.kraken.com/0/public/OHLC?pair='+endhtml)
    
    response=resp.json()
    
    responseinterstep = response['result']
    
    #get dictionary ticker symbol:
    for getdictionarytickersymbol in responseinterstep:
        dictionarytickersymbol = getdictionarytickersymbol
        break
    
    #after the next line responseinterstep contains a list of open high low close prices
    responseinterstep = responseinterstep[dictionarytickersymbol]
    
    closestorage = []
    for interval in responseinterstep:
        closestorage.append(interval[4])
    return closestorage


#
pricehistorylist = []
for i in tic:
    pricehistorylist.append(historical_data_close(i))

correlationlist = [[]]
count = 0



for i in range(0,len(tic)):
    
    correlationlist[count].append(tic[i])
    baseline = pricehistorylist[i]
    
    for j in range(0,len(tic)):
        
        if i!=j:
            
            checkedagainst = pricehistorylist[j]
            cora = stats.spearmanr(checkedagainst[-60:-2],baseline[-60:-2])
            #correlation filter
            if cora[0]>.8:
                correlationlist[count].append([tic[j],cora[0]])
            
            
    correlationlist.append([])
    count=count+1

