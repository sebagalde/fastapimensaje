from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Modelo de datos para el mensaje
class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    mensaje: str

app = FastAPI()


