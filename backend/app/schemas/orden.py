from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class DetalleOrdenCreate(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: Optional[float] = None

class OrdenCreate(BaseModel):
    detalles: List[DetalleOrdenCreate]

class DetalleOrdenOut(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    precio_unitario: float
    subtotal: float

    model_config = ConfigDict(from_attributes=True)  

class OrdenOut(BaseModel):
    id: int
    fecha: datetime
    total: float
    detalles: List[DetalleOrdenOut]

    model_config = ConfigDict(from_attributes=True)  