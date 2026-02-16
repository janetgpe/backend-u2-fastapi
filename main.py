from fastapi import FastAPI

app = FastAPI()  # crea la funcion

@app.get("/")    # decorador de funciones, Es una función que recibe otra función como argumento y devuelve una nueva función. 

# @app.get("/") es un decorador. Le dice a FastAPI: "Esta función debe ejecutarse cuando llegue una petición GET a la ruta / o sea ruta vacía"
# Con @app.get → función convertida en endpoint web.

# Un endpoint es un punto específico de acceso a un servicio web. Formalmente: Es la combinación de una URL (ruta) y un método HTTP que permite interactuar con un recurso del servidor.

def prueba():
    return {"Hola":"Mundo"}  # el valor es devuelto como un diccionario
