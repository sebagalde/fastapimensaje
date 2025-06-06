from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Modelo de datos para el mensaje
class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    mensaje: str

app = FastAPI()

# Simulación de base de datos en memoria
mensajes_db: List[Mensaje] = []

# GET: Obtener todos los mensajes
@app.get("/mensajes/", response_model=List[Mensaje])
def obtener_mensajes():
    return mensajes_db

# GET: Obtener un mensaje por ID
@app.get("/mensajes/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje_por_id(mensaje_id: int):
    for mensaje in mensajes_db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

# POST: Crear un nuevo mensaje
@app.post("/mensajes/", response_model=Mensaje)
def crear_mensaje(nuevo_mensaje: Mensaje):
    nuevo_mensaje.id = len(mensajes_db) + 1
    mensajes_db.append(nuevo_mensaje)
    return nuevo_mensaje

# PUT: Actualizar un mensaje por ID
@app.put("/mensajes/{mensaje_id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id: int, mensaje_actualizado: Mensaje):
    for index, mensaje in enumerate(mensajes_db):
        if mensaje.id == mensaje_id:
            mensaje_actualizado.id = mensaje_id
            mensajes_db[index] = mensaje_actualizado
            return mensaje_actualizado
    raise HTTPException(status_code=404, detail="Mensaje no encontrado para actualizar")

# DELETE: Eliminar un mensaje por ID
@app.delete("/mensajes/{mensaje_id}", response_model=dict)
def eliminar_mensaje(mensaje_id: int):
    for index, mensaje in enumerate(mensajes_db):
        if mensaje.id == mensaje_id:
            del mensajes_db[index]
            return {"detail": "Mensaje eliminado"}
    raise HTTPException(status_code=404, detail="Mensaje no encontrado para eliminar")
