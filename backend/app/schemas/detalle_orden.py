from pydantic import BaseModel, Field

class DetalleOrdenBase(BaseModel):
    """
    Esquema base para el detalle de una orden.

    Atributos:
        producto_id (int): Identificador del producto asociado.
        cantidad (int): Cantidad del producto en la orden (debe ser mayor a 0).
    """
    producto_id: int
    cantidad: int = Field(gt=0)

class DetalleOrdenCreate(DetalleOrdenBase):
    """
    Esquema para la creación de un detalle de orden.
    Hereda de DetalleOrdenBase.
    """
    pass

class DetalleOrdenOut(DetalleOrdenBase):
    """
    Esquema para la salida de un detalle de orden.

    Atributos adicionales:
        id (int): Identificador único del detalle de la orden.
        precio_unitario (float): Precio unitario del producto.
        subtotal (float): Subtotal calculado como cantidad * precio_unitario.
    """
    id: int
    precio_unitario: float
    subtotal: float

    class Config:
        """
        Configuración de Pydantic para permitir la conversión desde modelos ORM.
        """
        from_attributes = True