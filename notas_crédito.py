import pandas as pd
import numpy as np

df=pd.read_excel('notas_credito.xlsx')
#print(df.head())
#print(df.isnull().sum())

#decidi utilizar la mediana, pue slos valores que estaban en la columna eran enteros y estaban entre 1 y 3 por lo que 
#consideré que era una medida que no afectaría los datos de la columna.
df['CVE_VEND'] =df['CVE_VEND'].fillna(round(df['CVE_VEND'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#decidí utilizar ANT porque vi que era un nombre muy utilizado en esta columna
df['CVE_PEDI']=df['CVE_PEDI'].fillna('ANT')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#debido a que eran muchos nulos, decidi llenar los nulos con los datos siguientes a estos, y pensé que pasaría como con el
#dataset de devoluciones, sin embargo aqui con ffill fue suficiente.
df['FECHA_CANCELA'] =df['FECHA_CANCELA'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
print(valores_nulos)

df.to_csv('notas_credito_limpio.csv')