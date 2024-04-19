import pandas as pd
import numpy as np

df=pd.read_excel('devoluciones.xlsx')
#print(df.head())
#print(df.isnull().sum())

#decidi poner los valores de fecha con los siguientes a los nulos, sin embargo había muchos faltantes
df['FECHA_CANCELA'] =df['FECHA_CANCELA'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#por lo anterior fue necesario llenar los nulos con las fechas de los espacios anteriores a los nulos
df['FECHA_CANCELA'] =df['FECHA_CANCELA'].fillna(method='bfill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#aqui decidí sacar promedio y llenar con este los datos faltantes
df['CVE_VEND'] = df['CVE_VEND'].fillna(round(df['CVE_VEND'].mean(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#en este caso decidí llenar los nulos con los valores posteriores en la columna
df['CVE_PEDI'] =df['CVE_PEDI'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#en este caso preferí llenar lso nulos con los valores anteriores en la columna
df['DOC_ANT'] =df['DOC_ANT'].fillna(method='bfill')
valores_nulos=df.isnull().sum()
print(valores_nulos)

df.to_csv('devoluciones_limpio.csv')