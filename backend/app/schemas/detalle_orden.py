from pydantic import BaseModel, Field

class DetalleOrdenBase(BaseModel):
    producto_id: int
    cantidad: int = Field(gt=0)

class DetalleOrdenCreate(DetalleOrdenBase):
    pass

class DetalleOrdenOut(DetalleOrdenBase):
    id: int
    precio_unitario: float
    subtotal: float

    class Config:
        from_attributes = True
