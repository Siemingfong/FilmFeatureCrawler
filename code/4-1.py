import time 
import random
import datetime
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument('--headless')

#打開瀏覽器,確保你已經有chromedriver在你的目錄下
# 然後將options加入Chrome方法裡面，至於driver請用executable_path宣告進入
driver=webdriver.Chrome(executable_path=r'C:\Users\USER\Desktop\chromedriver_win32 (2)/chromedriver.exe',options=options)
dates=['2019-06-01','2019-07-01','2019-08-01','2019-09-01','2019-10-01','2019-11-01','2019-12-01','2020-01-01','2020-02-01','2020-03-01','2020-04-01','2020-05-01']
months=['Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun']
realmonths=['Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May']
prices={}
aaa=[0,0,0,0,0]
for i in realmonths:
    prices[i]=aaa
data1=[]
data2=[]
releasedates={}
for date,month,realmonth in zip(dates,months,realmonths):
    url = 'https://www.boxofficemojo.com/calendar/'+date
    driver.get(url)
    moviesss=driver.find_elements_by_xpath('//a[@class="a-link-normal"]//h3')
    for i in range(0,len(moviesss)):
        movies=driver.find_elements_by_xpath('//a[@class="a-link-normal"]//h3')
        movies[i].click()
        html = driver.page_source
        soup = bs(html,'lxml')
        table = soup.find_all('div',class_="a-section a-spacing-none")
        print(len(table))
        for j in table:
            s = j.find_all('span')
            if('Release Date' in s[0].text):
                releasedate=s[1].text
            elif('Widest Release' in s[0].text):
                widelyrelease=s[1].text
        releasedate=releasedate.split('-')[0]
        releasedate=releasedate.split('(')[0]
        print(widelyrelease)
        print(releasedate)
        k=str(releasedate).split()
        l=(str(widelyrelease).split())
        print(l[0].replace(',',''))
        data1.append(releasedate)
        data2.append(int(l[0].replace(',','')))
        if(k[0]==month):
            break
        if(releasedate not in releasedates):
            releasedates[releasedate]=0
        releasedates[releasedate]+=int(l[0].replace(',',''))

        print(driver.current_url)
print(releasedates)
Dates=[]
Numbers=[]
for i in releasedates:
    Dates.append(i)
    Numbers.append(releasedates[i])
print(Dates)
print(Numbers)


df1=pd.DataFrame()
df1['Date']=data1
df1['number of theaters']=data2
df1.to_csv(r'C:/Users/USER/Desktop/資訊/鄭恆安/csv/theaters.csv',encoding='big5',index=False)