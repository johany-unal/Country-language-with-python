import hashlib
import pandas as pd

## Obtener respuesta de https://restcountries.com/ idioma del pais

languaje= "portuguese"
lang=languaje.encode()

## Tomar el idioma y encriptarlo en SHA1
lang_sha1 = hashlib.sha1(lang)
lang_sha1_hex = lang_sha1.hexdigest() # Convierte a formato hexadecimal
print(lang_sha1_hex)

## Calcular tiempos




## Create dataframe

df=pd.DataFrame(columns=["Region", "City Name", "Language", "Time"])

print(df)
# Llenar el Dataframe

df_new=pd.DataFrame({'Region': [2, 4], 'City Name': [2, 0], 'Language': [2, 0],'Time': [2, 0]}, index=['falcon', 'dog'])



df_new2=pd.DataFrame({'Region': [56,3], 'City Name': [26,98], 'Language': [322, 50],'Time': [32, 40]},index=['falcata', 'doggy'])

df=pd.concat([df,df_new],sort=False)

df=pd.concat([df,df_new2],sort=False)

#df=df.append(df_new,ignore_index=True)

print(df)
## Calcular tiempo total, el tiempo promedio, el tiempo mínimo y el máximo que tardo



## Guardar en sqlite



## Generar  Json con la tabla y guardar en data.json
