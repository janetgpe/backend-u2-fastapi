import requests # libreria para hacer peticiones con python

respuesta = requests.get("http://127.0.0.1:8000")

# es get porque es el verbo a utilizar para sacar la url
# en requests se puso .get porque es el verbo que estamos usando en app.get("/")
# si hubiese puesto put, patch, update etc entonces sería requests.XXXXX
# esta ruta http://127.0.0.1:8000 sale cuando se levanta uvicorn nos indica porque ruta se esta ejecutando
print(respuesta) # responde si el servidor esta activo
print(respuesta.raw) # responde dando la dirección en memoria donde está el objeto
print(respuesta.text) # devuelve un string y ya no se considera el diccionario 
print(respuesta.json()) # responde con una cadena de texto tomada de un diccionario

diccionario=respuesta.json()
print(diccionario["Hola"])