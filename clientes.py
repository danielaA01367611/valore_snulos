import pandas as pd
import numpy as np

df=pd.read_excel('clientes.xlsx')
#print(df.head())
#print(df.isnull().sum())

#reemplacé este valor por un RFC generico, este dato se implanto en las columnas vacias
df['RFC'].fillna('XAXX010101000', inplace=True)
#print(df['RFC'])
#print(df['RFC'].isnull().sum())
#print(df.isnull().sum())

#decidí poner el nombre que se mostraba en la columna de RFC porque no había más información del cliente
df['NOMBRE'].fillna('MOSTR', inplace=True)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

df.to_csv('clientes_totales_limpio.csv')