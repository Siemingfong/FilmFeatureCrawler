from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
import random
import datetime
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import json
import requests
import io



url11='https://www.boxofficemojo.com/weekend/by-year/2019/?area=AU'
url12='https://www.boxofficemojo.com/weekend/by-year/2020/?area=AU'

url21='https://www.boxofficemojo.com/weekend/by-year/2019/?area=DE'
url22='https://www.boxofficemojo.com/weekend/by-year/2020/?area=DE'

url31='https://www.boxofficemojo.com/weekend/by-year/2019/?area=JP'
url32='https://www.boxofficemojo.com/weekend/by-year/2020/?area=JP'
url41='https://www.boxofficemojo.com/weekend/by-year/2019/'
url42='https://www.boxofficemojo.com/weekend/by-year/2020/'




#Australia
dates=[]
dfs1=pd.read_html(url11)
dfs2=pd.read_html(url12)
df11=pd.DataFrame()
df12=pd.DataFrame()
df21=pd.DataFrame()
df22=pd.DataFrame()
total1=pd.DataFrame()

df110=dfs1[0]['Overall Gross'][29::-1]
df12=dfs1[0]['Dates'][29::-1]
df210=dfs2[0]['Overall Gross'][:0:-1].replace(',','')
df22=dfs2[0]['Dates'][:0:-1]

k = []
for i in df110:
    k.append(int((i.replace('$','').replace(',',''))))
df11['Overall Gross']=k

k = []
for i in df210:
    k.append(int((i.replace('$','').replace(',',''))))
df21['Overall Gross']=k

for i in range(0,42):
    dates.append((datetime.datetime.strptime('2019-06-06','%Y-%m-%d')+datetime.timedelta(days=7*i)).date())
dates.append('2020-03-28')
dates.append('2020-06-04')

total1['Dates']=dates
total1['Overall Gross']=pd.concat([df11,df21],ignore_index=True)
print(total1)

total1.to_csv(r'C:/Users/USER/Desktop/資訊/鄭恆安/csv/Australia.csv',encoding='big5',index=False)



#Germany
dates=[]
dfs1=pd.read_html(url21)
dfs2=pd.read_html(url22)
df11=pd.DataFrame()
df12=pd.DataFrame()
df21=pd.DataFrame()
df22=pd.DataFrame()
total2=pd.DataFrame()


df110=dfs1[0]['Overall Gross'][29::-1]
df12=dfs1[0]['Dates'][29::-1]
df210=dfs2[0]['Overall Gross'][:0:-1].replace(',','')
df22=dfs2[0]['Dates'][:0:-1]


k = []
for i in df110:
    k.append(int((i.replace('$','').replace(',',''))))
df11['Overall Gross']=k

k = []
for i in df210:
    k.append(int((i.replace('$','').replace(',',''))))
df21['Overall Gross']=k

for i in range(0,42):
    dates.append((datetime.datetime.strptime('2019-06-06','%Y-%m-%d')+datetime.timedelta(days=7*i)).date())
dates.append('2020-04-09')
dates.append('2020-05-21')
dates.append('2020-05-28')
dates.append('2020-06-04')
total2['Dates']=dates
total2['Overall Gross']=pd.concat([df11,df21],ignore_index=True)
print(total2)
total2.to_csv(r'C:/Users/USER/Desktop/資訊/鄭恆安/csv/Germany.csv',encoding='big5',index=False)



#Japan
dates=[]
dfs1=pd.read_html(url31)
dfs2=pd.read_html(url32)
df11=pd.DataFrame()
df12=pd.DataFrame()
df21=pd.DataFrame()
df22=pd.DataFrame()
total=pd.DataFrame()


df110=dfs1[0]['Overall Gross'][29::-1]
df12=dfs1[0]['Dates'][29::-1]
df210=dfs2[0]['Overall Gross'][::-1].replace(',','')
df22=dfs2[0]['Dates'][::-1]
k = []
for i in df110:
    k.append(int((i.replace('$','').replace(',',''))))
df11['Overall Gross']=k

k = []
for i in df210:
    k.append(int((i.replace('$','').replace(',',''))))
df21['Overall Gross']=k

for i in range(0,44):
    dates.append((datetime.datetime.strptime('2019-06-06','%Y-%m-%d')+datetime.timedelta(days=7*i)).date())

dates.append('2020-05-14')
dates.append('2020-05-21')
dates.append('2020-05-28')
dates.append('2020-06-04')

#print(len(pd.concat([df12,df22])))
total['Dates']=dates
total['Overall Gross']=pd.concat([df11,df21],ignore_index=True)
print(total)
total.to_csv(r'C:/Users/USER/Desktop/資訊/鄭恆安/csv/Japan.csv',encoding='big5',index=False)



#NorthAmerica
dates=[]
dfs1=pd.read_html(url41)
dfs2=pd.read_html(url42)
df11=pd.DataFrame()
df12=pd.DataFrame()
df21=pd.DataFrame()
df22=pd.DataFrame()
total=pd.DataFrame()


df110=pd.concat([dfs1[0]['Overall Gross'][33:20:-1],dfs1[0]['Overall Gross'][19:13:-1],dfs1[0]['Overall Gross'][12:6:-1],dfs1[0]['Overall Gross'][4::-1]],ignore_index=True)
df12=pd.concat([dfs1[0]['Dates'][33:20:-1],dfs1[0]['Dates'][19:13:-1],dfs1[0]['Dates'][12:6:-1],dfs1[0]['Dates'][4::-1]],ignore_index=True)
df210=pd.concat([dfs2[0]['Overall Gross'][27:25:-1],dfs2[0]['Overall Gross'][24:20:-1],dfs2[0]['Overall Gross'][19:11:-1],dfs2[0]['Overall Gross'][10:4:-1],dfs2[0]['Overall Gross'][3::-1]],ignore_index=True)
df22=pd.concat([dfs2[0]['Dates'][27:25:-1],dfs2[0]['Dates'][24:20:-1],dfs2[0]['Dates'][19:11:-1],dfs2[0]['Dates'][10:4:-1],dfs2[0]['Dates'][3::-1]],ignore_index=True)

k = []
for i in df110:
    k.append(int((i.replace('$','').replace(',',''))))
df11['Overall Gross']=k

k = []
for i in df210:
    k.append(int((i.replace('$','').replace(',',''))))
df21['Overall Gross']=k

for i in range(0,54):
    dates.append((datetime.datetime.strptime('2019-06-06','%Y-%m-%d')+datetime.timedelta(days=7*i)).date())
total['Dates']=dates
total['Overall Gross']=pd.concat([df11,df21],ignore_index=True)
print(total)
total.to_csv(r'C:/Users/USER/Desktop/資訊/鄭恆安/csv/NorthAmerica.csv',encoding='big5',index=False)




