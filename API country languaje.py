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
country=("peru","colombia","ecuador")
#print(country)
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







