import pandas as pd
import numpy as np


#Carga desde un archivo .xlsx sin indice
df=pd.read_csv("ventas_totales.csv")
#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

#quitar nulo en columna salon_ventas
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#quitar nulo en columna tarjetas_debito
df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#quitar nulo en columna tarjetas_credito
df['tarjetas_credito'] = df['tarjetas_credito'].fillna(round(df['tarjetas_credito'].median(),1))
valores_nulos=df.isnull().sum()
print(valores_nulos)
     