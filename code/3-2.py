import pandas as pd
import requests
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
df1=pd.read_csv(r'C:/Users/USER/Desktop/資訊/鄭恆安/csv/Australia.csv',encoding='big5')
df2=pd.read_csv(r'C:/Users/USER/Desktop/資訊/鄭恆安/csv/Germany.csv',encoding='big5')
df3=pd.read_csv(r'C:/Users/USER/Desktop/資訊/鄭恆安/csv/Japan.csv',encoding='big5')
df4=pd.read_csv(r'C:/Users/USER/Desktop/資訊/鄭恆安/csv/NorthAmerica.csv',encoding='big5')
ay=df1['Overall Gross']
ax=df1['Dates']
ax = pd.to_datetime(ax) 

by=df2['Overall Gross']
bx=df2['Dates']
bx = pd.to_datetime(bx) 

cy=df3['Overall Gross']
cx=df3['Dates']
cx = pd.to_datetime(cx) 

dy=df4['Overall Gross']
dx=df4['Dates']
dx = pd.to_datetime(dx) 
plt.plot(ax,ay, label='Australia')
plt.plot(bx,by, label='Germany')
plt.plot(cx,cy, label='Japan')
plt.plot(dx,dy, label='NorthAmerica')
plt.legend()
plt.xlabel('time')
plt.ylabel('profit')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  #設定x軸主刻度顯示格式（日期）
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.show()
