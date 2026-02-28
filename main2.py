# Hola mundo con FatAPI

from fastapi import FastAPI

app = FastAPI()  

@app.get("/")    

def prueba():
    return {"Hola":"Mundo"}  