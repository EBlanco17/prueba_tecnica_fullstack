from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from app.schemas.detalle_orden import DetalleOrdenCreate, DetalleOrdenOut

class OrdenBase(BaseModel):
    total: float

class OrdenCreate(BaseModel):
    detalles: List[DetalleOrdenCreate]

class OrdenOut(BaseModel):
    id: int
    fecha: datetime
    total: float
    detalles: List[DetalleOrdenOut]

class Config:
    orm_mode = True
