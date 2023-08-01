import pandas as pd
from binance.client import Client
import time

client = Client("xxxxx", "xxxxxxx")

coins = ["OPUSDT"]
start = time.time()
klines = client.get_historical_klines(coins[0], Client.KLINE_INTERVAL_5MINUTE, "27 July, 2023", "31 July, 2023")

# Extracting the relevant columns from the data
data = [[candlestick[0], candlestick[1], candlestick[2], candlestick[3], candlestick[4]] for candlestick in klines]
columns = ["Open time", "Open", "High", "Low", "Close"]
df = pd.DataFrame(data, columns=columns)
# Unix time stamps to datetime objects conversion
df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
df[['Open', 'High', 'Low', 'Close']] = df[['Open', 'High', 'Low', 'Close']].apply(pd.to_numeric)

# Calculate percentage change from Open to Close price and add it as a new column
df['pct_change'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# Initialize Profit column with NaN values
df['Profit'] = float('nan')
print(df)
pozisyon = 0  # 1 ise pozisyon açık, 0 ise kapalı.
bakiye = 1000  # usdt
tp = 0.98
commission_rate = 0.0015  # 0.1% commission
poz_tutar=100 #usdt


for i in range(len(df) - 2):
    if df.loc[i, 'pct_change'] > 0.1 and df.loc[i+1, 'pct_change'] > 0.1 and df.loc[i+2, 'pct_change'] > 0.1 and pozisyon == 0:
        pozisyon = 1
        adet=round(poz_tutar/df.loc[i+3, 'Open'],0)
        print("\n---------------------\n")
        print("Short pozisyon açılmıştır.  ", "Tarih:", df.loc[i+3, 'Open time'], "   Giriş Fiyatı: ", df.loc[i+3, 'Open'] , "Adet: " , adet  )
        ##açılan pozisyonun index değeri i+3 'tür.

        # takeprofit
        found = False

        for k in range(36):
            if df.loc[i+3, 'Open'] * tp > df.loc[i+3+k, 'Low']:
                print("Short pozisyon kapanmıştır.  ", "Tarih:", df.loc[i+3+k, 'Open time'], "   Çıkış Fiyatı: ", df.loc[i+3, 'Open'] * tp)
                kar_tutari = poz_tutar * (1 - tp - commission_rate)  # Deduct commission from profit
                bakiye = bakiye + kar_tutari
                print("Yüzde ", round(100*(1 - tp ), 2), " kar edildi. ", "Pozisyon karı: ", kar_tutari, "  Bakiye: ", bakiye)
                pozisyon = 0
                found = True
                poz_tutar=100 #usdt
                break

        if not found:
            print(df.loc[i+3+k+1, 'Open time'], " tarihinde pozisyonu durduruluyor.")
            print("Kar-Zarar oranı:")
            kar_zarar_orani = (df.loc[i+3, 'Open'] - df.loc[i+3+k+1, 'Open']) / df.loc[i+3, 'Open']-commission_rate
            print(kar_zarar_orani)
            kar_tutari = poz_tutar * kar_zarar_orani
            bakiye = bakiye + kar_tutari
            print("Pozisyon karı: ", kar_tutari, "  Bakiye: ", bakiye)
            pozisyon = 0
            if bakiye<1000:
                poz_tutar=poz_tutar*1.1 #usdt
            else:
                poz_tutar=100
print("Son Bakiye: ", bakiye)
