# Hola mundo con FatAPI

import requests 

respuesta = requests.get("http://127.0.0.1:8000")

print(respuesta) 
print(respuesta.raw) 
print(respuesta.text) 
print(respuesta.json()) 

diccionario=respuesta.json()
print(diccionario["Hola"])