from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class DetalleOrdenCreate(BaseModel):
    """
    Esquema para la creación de un detalle de orden.

    Atributos:
        producto_id (int): Identificador del producto asociado.
        cantidad (int): Cantidad del producto en la orden.
        precio_unitario (Optional[float]): Precio unitario del producto (opcional).
    """
    producto_id: int
    cantidad: int
    precio_unitario: Optional[float] = None

class OrdenCreate(BaseModel):
    """
    Esquema para la creación de una orden.

    Atributos:
        detalles (List[DetalleOrdenCreate]): Lista de detalles de la orden.
    """
    detalles: List[DetalleOrdenCreate]

class DetalleOrdenOut(BaseModel):
    """
    Esquema para la salida de un detalle de orden.

    Atributos:
        id (int): Identificador único del detalle de la orden.
        producto_id (int): Identificador del producto asociado.
        cantidad (int): Cantidad del producto en la orden.
        precio_unitario (float): Precio unitario del producto.
        subtotal (float): Subtotal calculado como cantidad * precio_unitario.
    """
    id: int
    producto_id: int
    cantidad: int
    precio_unitario: float
    subtotal: float

    model_config = ConfigDict(from_attributes=True)

class OrdenOut(BaseModel):
    """
    Esquema para la salida de una orden.

    Atributos:
        id (int): Identificador único de la orden.
        fecha (datetime): Fecha y hora en que se creó la orden.
        total (float): Total de la orden.
        detalles (List[DetalleOrdenOut]): Lista de detalles de la orden.
    """
    id: int
    fecha: datetime
    total: float
    detalles: List[DetalleOrdenOut]

    model_config = ConfigDict(from_attributes=True)