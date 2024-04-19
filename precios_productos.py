import pandas as pd
import numpy as np

df=pd.read_excel('precios_productos.xlsx')
#print(df.head())
#print(df.isnull().sum())

#decidi imputar el nombre de Leticia Ramirez Hernandez porque er el anterior y el de después de los datos faltantes, por lo que lo mñas seguro es
#que estos dos productos que tenian nulos fueran de la misma vendedora.
df['NOMBRE_VENDEDOR']=df['NOMBRE_VENDEDOR'].fillna('LETICIA RAMIREZ HERNANDEZ')
valores_nulos=df.isnull().sum()
print(valores_nulos)

df.to_csv('precios_productos_limpio.csv')