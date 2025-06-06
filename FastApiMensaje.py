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
