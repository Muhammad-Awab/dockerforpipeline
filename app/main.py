# Imports necesarios
from fastapi import FastAPI
from pydantic import BaseModel

app : FastAPI = FastAPI()

'''
Funcion para procesar un mensaje dado por el usuario (msg).
En esta funcion se aplican tecnicas de _prompt engineering_
'''
def process(msg : str) -> str:
    return msg + " PROCESADO!"

'''
Clase que detalla el cuerpo de una peticion POST
enviada por el cliente.
Esta peticion contendra el mensaje (campo msg) enviado
por el usuario para la IAGen y su usuario (campo user) 
'''
class IAGenMsg(BaseModel):
    user : str
    msg  : str

'''
Clase que detalla el cuerpo de una respuesta a una peticion POST
enviada por el cliente.
Esta peticion contendrá el mensaje respondido por la IAGen (campo response) y el usuario
al que esta respondiendo (campo user) 
'''
class IAGenResponse(BaseModel):
    user : str
    response  : str



'''
Endpoint para recibir una respuesta de la IAGen 
dado un mensaje introducido por el usuario (msg).
Para acceder al endpoint es NECESARIO introducir un usuario valido (user).
De lo contrario, obtendremos un error.

Realiza una peticion HTTP POST al servidor (de esta manera podemos aceptar un json).
'''
@app.post("/response/")
async def getResponse(userMsg : IAGenMsg) -> dict:
    
    # AQUI SE DEBERÍA PROCESAR MSG!
    processed : str = process(userMsg.msg)

    # Creamos la respuesta y la devolvemos
    response : IAGenResponse = IAGenResponse(user=userMsg.user, response=processed)

    return response.model_dump()