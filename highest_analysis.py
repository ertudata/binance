from binance.client import Client
client = Client("xxxxx", "xxxxx")

import pandas as pd
import datetime
import time
#spot coins
#coins=['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT', 'ETCUSDT', 'LINKUSDT', 'XLMUSDT', 'ADAUSDT', 'XMRUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT', 'BATUSDT', 'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT', 'COMPUSDT', 'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT', 'SNXUSDT', 'DOTUSDT', 'DEFIUSDT', 'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'RUNEUSDT', 'SUSHIUSDT', 'SRMUSDT', 'EGLDUSDT', 'SOLUSDT', 'ICXUSDT', 'STORJUSDT', 'BLZUSDT', 'UNIUSDT', 'AVAXUSDT', 'FTMUSDT', 'HNTUSDT', 'ENJUSDT', 'FLMUSDT', 'TOMOUSDT', 'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'RSRUSDT', 'LRCUSDT', 'MATICUSDT', 'OCEANUSDT', 'CVCUSDT', 'BELUSDT', 'CTKUSDT', 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT', 'GRTUSDT', '1INCHUSDT', 'CHZUSDT', 'SANDUSDT', 'ANKRUSDT', 'BTSUSDT', 'LITUSDT', 'UNFIUSDT', 'REEFUSDT', 'RVNUSDT', 'SFPUSDT', 'XEMUSDT', 'BTCSTUSDT', 'COTIUSDT', 'CHRUSDT', 'MANAUSDT', 'ALICEUSDT', 'HBARUSDT', 'ONEUSDT', 'LINAUSDT', 'STMXUSDT', 'DENTUSDT', 'CELRUSDT', 'HOTUSDT', 'MTLUSDT', 'OGNUSDT', 'NKNUSDT', 'SCUSDT', 'DGBUSDT', '1000SHIBUSDT', 'BAKEUSDT', 'GTCUSDT', 'BTCDOMUSDT', 'TLMUSDT', 'IOTXUSDT', 'AUDIOUSDT', 'RAYUSDT', 'C98USDT', 'MASKUSDT', 'ATAUSDT', 'DYDXUSDT', '1000XECUSDT', 'GALAUSDT', 'CELOUSDT', 'ARUSDT', 'KLAYUSDT', 'ARPAUSDT', 'CTSIUSDT', 'LPTUSDT', 'ENSUSDT', 'PEOPLEUSDT', 'ANTUSDT', 'ROSEUSDT', 'DUSKUSDT', 'FLOWUSDT', 'IMXUSDT', 'API3USDT', 'GMTUSDT', 'APEUSDT', 'WOOUSDT', 'FTTUSDT', 'JASMYUSDT', 'DARUSDT', 'GALUSDT', 'OPUSDT', 'INJUSDT', 'STGUSDT', 'FOOTBALLUSDT', 'SPELLUSDT', '1000LUNCUSDT', 'LUNA2USDT', 'LDOUSDT', 'CVXUSDT', 'ICPUSDT', 'APTUSDT', 'QNTUSDT', 'BLUEBIRDUSDT', 'FETUSDT', 'FXSUSDT', 'HOOKUSDT', 'MAGICUSDT', 'TUSDT', 'RNDRUSDT', 'HIGHUSDT', 'MINAUSDT', 'ASTRUSDT', 'AGIXUSDT', 'PHBUSDT', 'GMXUSDT', 'CFXUSDT', 'STXUSDT', 'COCOSUSDT', 'BNXUSDT']

#futurecoins
coins=['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT']
      ## 'EOSUSDT', 'LTCUSDT', 'TRXUSDT', 'ETCUSDT', 'LINKUSDT', 'XLMUSDT', 'ADAUSDT', 'XMRUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT', 'BATUSDT', 'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT', 'COMPUSDT', 'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT', 'SNXUSDT', 'DOTUSDT', 'DEFIUSDT', 'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'RUNEUSDT', 'SUSHIUSDT', 'SRMUSDT', 'EGLDUSDT', 'SOLUSDT', 'ICXUSDT', 'STORJUSDT', 'BLZUSDT', 'UNIUSDT', 'AVAXUSDT', 'FTMUSDT', 'HNTUSDT', 'ENJUSDT', 'FLMUSDT', 'TOMOUSDT', 'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'RSRUSDT', 'LRCUSDT', 'MATICUSDT', 'OCEANUSDT', 'CVCUSDT', 'BELUSDT', 'CTKUSDT', 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT', 'GRTUSDT', '1INCHUSDT', 'CHZUSDT', 'SANDUSDT', 'ANKRUSDT', 'BTSUSDT', 'LITUSDT', 'UNFIUSDT', 'REEFUSDT', 'RVNUSDT', 'SFPUSDT', 'XEMUSDT', 'BTCSTUSDT', 'COTIUSDT', 'CHRUSDT', 'MANAUSDT', 'ALICEUSDT', 'HBARUSDT', 'ONEUSDT', 'LINAUSDT', 'STMXUSDT', 'DENTUSDT', 'CELRUSDT', 'HOTUSDT', 'MTLUSDT', 'OGNUSDT', 'NKNUSDT', 'SCUSDT', 'DGBUSDT', '1000SHIBUSDT', 'BAKEUSDT', 'GTCUSDT', 'BTCDOMUSDT', 'IOTXUSDT', 'AUDIOUSDT', 'RAYUSDT', 'C98USDT', 'MASKUSDT', 'ATAUSDT', 'DYDXUSDT', '1000XECUSDT', 'GALAUSDT', 'CELOUSDT', 'ARUSDT', 'KLAYUSDT', 'ARPAUSDT', 'CTSIUSDT', 'LPTUSDT', 'ENSUSDT', 'PEOPLEUSDT', 'ANTUSDT', 'ROSEUSDT', 'DUSKUSDT', 'FLOWUSDT', 'IMXUSDT', 'API3USDT', 'GMTUSDT', 'APEUSDT', 'WOOUSDT', 'FTTUSDT', 'JASMYUSDT', 'DARUSDT', 'GALUSDT', 'OPUSDT', 'INJUSDT', 'STGUSDT', 'FOOTBALLUSDT', 'SPELLUSDT', '1000LUNCUSDT', 'LUNA2USDT', 'LDOUSDT', 'CVXUSDT', 'ICPUSDT', 'APTUSDT', 'QNTUSDT', 'BLUEBIRDUSDT', 'FETUSDT', 'FXSUSDT', 'HOOKUSDT', 'MAGICUSDT', 'TUSDT', 'RNDRUSDT', 'HIGHUSDT', 'MINAUSDT', 'ASTRUSDT', 'AGIXUSDT', 'PHBUSDT', 'GMXUSDT', 'CFXUSDT', 'STXUSDT', 'COCOSUSDT', 'BNXUSDT', 'ACHUSDT', 'SSVUSDT', 'CKBUSDT', 'PERPUSDT', 'TRUUSDT', 'LQTYUSDT', 'USDCUSDT', 'IDUSDT', 'ARBUSDT', 'JOEUSDT', 'TLMUSDT', 'AMBUSDT', 'LEVERUSDT', 'RDNTUSDT', 'HFTUSDT', 'XVSUSDT', 'BLURUSDT', 'EDUUSDT', 'IDEXUSDT', 'SUIUSDT', '1000PEPEUSDT', '1000FLOKIUSDT', 'UMAUSDT', 'RADUSDT', 'KEYUSDT', 'COMBOUSDT', 'NMRUSDT', 'MAVUSDT', 'MDTUSDT', 'XVGUSDT']
i=0

all_data = pd.DataFrame()
while i<len(coins):
    try:
        start = time.time()
        klines = client.get_historical_klines(coins[i], Client.KLINE_INTERVAL_1MONTH, "07 July, 2020", "15 July, 2023")
        klines = list(klines)
        # create dataframe from the klines data
        df = pd.DataFrame(klines, columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"])
        df = df.drop(['Taker buy base asset volume', 'Quote asset volume','Taker buy quote asset volume', "Close time",'Ignore',"Volume"], axis=1)
        print(coins[i])
        df['coin']=coins[i]
        df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
        df[['Open', 'High', 'Low', 'Close', 'Number of trades']] = df[['Open', 'High', 'Low', 'Close', 'Number of trades']].astype(float)

        #df= df.iloc[[0]]
        k=-1
        while k>-5:
            tarih=df['Open time'].iloc[k]
            df[tarih] = df['High'].iloc[k]
            df = df.iloc[k]
            k=k-1
        print(df)
        all_data = all_data.append(df, ignore_index=True)
        end = time.time()
        print("Time taken: ", end - start, "seconds.")

        i=i+1
    except:
        print("devam")
        i=i+1



print(all_data)
all_data.to_excel(f"{'highest_analysis'}{'15juy'}.xlsx", sheet_name='Sheet1', index=True)
