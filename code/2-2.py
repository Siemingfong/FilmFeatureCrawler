import pandas as pd
import requests
import matplotlib.pyplot as plt 



df = pd.read_csv(r'C:\Users\USER\Desktop\資訊\鄭恆安\csv\number_of_films.csv',encoding='big5') 
df.plot(x='month', y='number', color='Green', label='number of films')
plt.show()