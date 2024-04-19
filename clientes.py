import pandas as pd
import numpy as np

df=pd.read_excel('clientes.xlsx')
#print(df.head())
#print(df.isnull().sum())

df['RFC'].fillna('XAXX010101000', inplace=True)
#print(df['RFC'])
#print(df['RFC'].isnull().sum())
#print(df.isnull().sum())

df['NOMBRE'].fillna('MOSTR', inplace=True)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

df.to_csv('clientes_totales_limpio.csv')