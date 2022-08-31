import hashlib
import pandas as pd
import requests
import time
import numpy as np
import sqlite3
import json

## Create dataframe

df=pd.DataFrame(columns=["Region", "City Name", "Language", "Time"]) #Creamos dataframe vacio




## Tomar el idioma y encriptarlo en SHA1
def encriptar(languaje):
    lang=languaje.encode()
    lang_sha1 = hashlib.sha1(lang)
    lang_sha1_hex = lang_sha1.hexdigest() # Convierte a formato hexadecimal
    return(lang_sha1_hex)   # Retorna el lenguaje encriptado en SHA1.


def generate_site(number_country):          # Se le ingresa un número de la lista de paises
    site="https://restcountries.com/v2/name/"+country[number_country]
    print(site)
    return site                             # Retorna el http que donde se debe capturar la informacion del pais

def capture_info(number_country):
    start = time.process_time()
    
    site=generate_site(number_country) ##generar sitio a consultar.
    
    r=requests.get(site)
    j=r.json()
    j1=j[0]
    
    print(j1['region'])
    region=j1['region']
    print(j1['capital'])
    capital=j1['capital']
    j2=j1['languages'][0]
    language= j2['name']
    lang_encrip=encriptar(language) # Encriptar el lenguaje, llamano a la función

    end = time.process_time()
    time_used=end - start           # Calculamos el tiempo empleado en armar la fila 

    info=[region, capital,lang_encrip,time_used] # añadimos la info a una lista

    return info
    

def complete_dataframe(number_country,df,region, capital,lang_encrip,time_used):  # Llenar el Dataframe, añadiebndo una nueva fila.
    df_new=pd.DataFrame({'Region': region, 'City Name': capital, 'Language': lang_encrip,'Time': time_used}, index=number_country) # Convertir info en dicccionario

    df=pd.concat([df,df_new],sort=False)
    
    
    return df
    
 

## Lista de paises a investigar. Es una varible general.
#country=("peru","colombia","ecuador","argentina","panama","peru")
country=("peru","colombia","ecuador","argentina","panama","peru","china","india","iran","japan","pakistan","australia","chile","venezuela","brazil","canada","cuba","jamaica","mexico","belize","guatemala","honduras","nicaragua","panama","denmark","france","germany","italy","portugal","russia","spain","turkey","angola","cameroon","egypt","morocco","nigeria","uganda")

#print(country)
country_count=0     # variable cuenta la cantidad de paises consultados

## Create dataframe
df=pd.DataFrame(columns=["Region", "City Name", "Language", "Time"]) #Creamos dataframe vacio


## CREAR CADA REGISTRO DE LA TABLA (se repite cada registro)


while country_count<len(country):
    info=capture_info(country_count)
    print(info)
    region=info[0]
    capital=info[1]
    lang_encrip=info[2]
    time_used=info[3]

    new_fila={'Region': region, 'City Name': capital, 'Language': lang_encrip,'Time': time_used}
    print(new_fila)

    df=df.append(new_fila,ignore_index=True)

    country_count +=1  # sumamos 1 al contador de country


print (df) # imprimimos el dataframe en consola


## Calcular tiempo total, el tiempo promedio, el tiempo mínimo y el máximo que tardo

minimum=df['Time'].min()
maximum=df['Time'].max()
mean=df['Time'].mean()
total=df['Time'].sum()
print("el tiempo mínimo de construción de una fila fue "+ str(minimum) + " segundos")
print("el tiempo mínimo de construción de una fila fue "+ str(df['Time'].max()) +" segundos")
print("el tiempo promedio de construción de una fila fue "+ str(mean) + " segundos")
print("el tiempo total de construción del dataframe fue "+ str(total) + " segundos")


## Guardar en sqlite

conn=sqlite3.connect("mydb.db")
cursor=conn.cursor()
df.to_sql("country_information",conn,if_exists="replace")
cursor.execute("SELECT * FROM country_information").fetchall()
   
conn.close()




## Generar  Json con la tabla y guardar en data.json



data = df.to_json(orient = 'columns')

print(data)     # visualizamos la tabla en formato json

with open('data.json', 'w') as file:  #guardamos la tabla en formato json
    json.dump(data, file, indent=4)



