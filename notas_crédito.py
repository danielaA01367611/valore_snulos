import pandas as pd
import numpy as np

df=pd.read_excel('notas_credito.xlsx')
#print(df.head())
#print(df.isnull().sum())

df['CVE_VEND'] =df['CVE_VEND'].fillna(round(df['CVE_VEND'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

df['CVE_PEDI']=df['CVE_PEDI'].fillna('ANT')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

df['FECHA_CANCELA'] =df['FECHA_CANCELA'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
print(valores_nulos)

df.to_csv('notas_credito_limpio.csv')