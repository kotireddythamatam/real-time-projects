import urllib.request
import pandas
import csv
import matplotlib.pyplot
import sys
print("""select options:
1.GOOG
2.CSCO
3.AAPL
4.FB
5.ORCL
6.AMZN
7.INTL
8.BAC
9.TSLA
10.BCS
11.IBM
12.GS
13.CRM
14.C
15.MSFT
16.GE
17.JNJ
18.GM""")
share_values=input("which company share values you want:").upper()
a=urllib.request.urlopen("http://api.kibot.com/?action=login&user=guest&password=guest")
b=urllib.request.urlopen("http://api.kibot.com/?action=history&symbol="+str(share_values)+"&interval=daily&period="+sys.argv[1])
c=b.read()
d=c.decode('utf-8')
e=d.split()
print(e)
f=[]
for g in e:
    h=g.split(',')
    i=f.append(h)
print(f)
df=pandas.DataFrame(data=f,columns=['date','open','high','low','average','products'])
print(df)
df.to_csv("share values"+str(share_values)+".csv",index=None,header=True)
df=pandas.read_csv("share values"+str(share_values)+".csv")
print(df['open'].max())
print(df['high'].max())
print(df['low'].max())
print(df['average'].max())
print(df['products'].max())
print(df['open'].min())
print(df['high'].min())
print(df['low'].min())
print(df['average'].min())
print(df['products'].min())
print(df['open'].std())
print(df['high'].std())
print(df['low'].std())
print(df['average'].std())
print(df['products'].std())
print(df['open'].mean())
print(df['high'].mean())
print(df['low'].mean())
print(df['average'].mean())
print(df['products'].mean())
matplotlib.pyplot.plot(list(df['high']),color="g")
matplotlib.pyplot.title(share_values)
matplotlib.pyplot.xlabel("days")
matplotlib.pyplot.ylabel("share values")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
