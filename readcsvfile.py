#https://tomokichi.blog/%E3%80%90python%E3%80%91csv%E3%81%8B%E3%82%89%E3%82%B0%E3%83%A9%E3%83%95%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B/
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import matplotlib.dates as mdates
#--------------------------------------------------------------------------
data = pd.read_csv('C:\\Users\\User\\Downloads\\nhk_news_covid19_prefectures_daily_data.csv', encoding='utf8')
#print(data)

x = data['日付']
a = data['都道府県名']
y = data['各地の感染者数_1日ごとの発表数']

datax = []
datay = []
for xi, ai, yi in zip(x, a, y):
  #print(xi)
  #print(ai)
  #print(yi)
  if ai == '東京都':
  #if ai == '千葉県':
    datax.append(xi)
    datay.append(yi)
    #print(xi)
    #print(yi)

#なぜか日付が1970からになる
#https://qiita.com/damyarou/items/19f19658b618fd05b3b6
ss = []

ss=pd.to_datetime(datax, format='%Y/%m/%d')

#plt.plot(datax,datay)
plt.plot(ss,datay)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
plt.savefig('C:\\Users\\User\\Documents\\Python\\outcovid19.png', dpi=300, orientation='portrait', transparent=False)

