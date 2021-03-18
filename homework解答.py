import time 
import random
import datetime
from bs4 import BeautifulSoup
import pandas as pd
import os
import json
import requests

month=['01','02','03','04','05','06','07','08','09','10','11','12']
year=['2015','2016','2017','2018','2019','2020']
date=[]
movies=[]

def craw(startdate,enddate):
    url = 'https://www.imdb.com/search/title/?title_type=feature&release_date='+startdate+','+enddate
    html=requests.get(url).text
    soup = BeautifulSoup(html,'lxml')
    #小考: 爬取整串文字 ex.1-50 of 666 titles 並存入count變數
    div = soup.find('div',class_='desc')
    count = div.find('span').text
    
    # 另解 count = soup.select_one('#main > div > div.nav > div.desc > span:nth-child(1)').text (和上面那兩行功能一樣)
    count = count.split()
    print(count[2])
    return count[2]

for i in range(0,6):
    for j in range(0,12):
        startdate=year[i]+'-'+month[j]+'-01'
        if(month[j]=='12'):
            enddate=str(int(year[i])+1)+'-01-01'
        else:
            enddate=year[i]+'-'+month[j+1]+'-01'
        date.append(year[i]+'-'+month[j])
        movies.append(int(craw(startdate,enddate).replace(',','')))

df= pd.DataFrame()
df['month']=date
df['number']=movies
print(df)





