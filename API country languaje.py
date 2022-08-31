import hashlib
import pandas as pd
import requests
import time

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
    #print(j)
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
    
    
    
    return 0

def complete_dataframe(number_country,df,region, capital,lang_encrip,time_used):  # Llenar el Dataframe, añadiebndo una nueva fila.
    df_new=pd.DataFrame({'Region': region, 'City Name': capital, 'Language': lang_encrip,'Time': time_used}, index=number_country) # Convertir info en dicccionario

    df=pd.concat([df,df_new],sort=False)
    
    
    return df
    
    
#start = time.process_time()

## Lista de paises a investigar. Es una varible general.
#country=("peru","colombia","ecuador")

##generar sitio a consultar.

#site="https://restcountries.com/v2/name/"+country[2]

#r=requests.get("https://restcountries.com/v3.1/all")
#r=requests.get("https://restcountries.com/v3.1/lang/spa")
r=requests.get("https://restcountries.com/v2/name/peru")
#r=requests.get(site)

j=r.json()
#print(j)
j1=j[0]
print(j1['region'])
print(j1['capital'])

j2=j1['languages'][0]

print(j2['name'])
#r1=requests.get("https://restcountries.com/v2/region/europe")
#j_region=r1.json()
#print(j_region)

#lang_sha1_hex=12

# Convertir info en dicccionario
def country_info(region,city_name,lang_sha1_hex, time):
    h={'Region': region, 'City Name': city_name, 'Language': lang_sha1_hex,'Time': time}
    return h







## Calcular tiempos


#print(df)
# Llenar el Dataframe

#df_new=pd.DataFrame({'Region': [2, 4], 'City Name': [2, 0], 'Language': lang_sha1_hex,'Time': [2, 0]}, index=['falcon', 'dog'])



#df_new2=pd.DataFrame({'Region': [56,3], 'City Name': [26,98], 'Language': [322, 50],'Time': [32, 40]}, index=['falcon', 'dog'])

#df_new3=pd.DataFrame(country_info("Egipto","El Cairo","gerf563t343",0.345), index=['falcon', 'dog'])

#df=pd.concat([df,df_new],sort=False)

#df=pd.concat([df,df_new2],sort=False)

#df=pd.concat([df,df_new3],ignore_index=True)

#complete_dataframe(4)

#print(df)
## Calcular tiempo total, el tiempo promedio, el tiempo mínimo y el máximo que tardo



## Guardar en sqlite



## Generar  Json con la tabla y guardar en data.json







































## Lista de paises a investigar. Es una varible general.
country=("peru","colombia","ecuador")
country_count=0     # variable cuenta la cantidad de paises consultados

## Create dataframe
df=pd.DataFrame(columns=["Region", "City Name", "Language", "Time"]) #Creamos dataframe vacio


## CREAR CADA REGISTRO DE LA TABLA (se repite cada registro)


info=capture_info(country_count)
print(info)
country_count +=1  # sumamos 1 al contador de country



## Calcular tiempos



## Calcular tiempo total, el tiempo promedio, el tiempo mínimo y el máximo que tardo
## Calcular tiempo total, el tiempo promedio, el tiempo mínimo y el máximo que tardo
## Guardar en sqlite
## Generar  Json con la tabla y guardar en data.json







