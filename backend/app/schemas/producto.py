from pydantic import BaseModel, Field, ConfigDict

class ProductoBase(BaseModel):
    """
    Esquema base para un producto.

    Atributos:
        nombre (str): Nombre del producto.
        cantidad_disponible (int): Cantidad disponible en inventario (debe ser mayor o igual a 0).
        precio_unitario (float): Precio unitario del producto (debe ser mayor a 0).
    """
    nombre: str
    cantidad_disponible: int = Field(gt=-1)
    precio_unitario: float = Field(gt=0)

class ProductoCreate(ProductoBase):
    """
    Esquema para la creación de un producto.
    Hereda de ProductoBase.
    """
    pass

class ProductoOut(ProductoBase):
    """
    Esquema para la salida de un producto.

    Atributos adicionales:
        id (int): Identificador único del producto.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)

class ProductoTopOut(BaseModel):
    """
    Esquema para la salida de los productos más vendidos.

    Atributos:
        nombre (str): Nombre del producto.
        total_comprado (int): Cantidad total comprada del producto.
    """
    nombre: str
    total_comprado: int

    model_config = ConfigDict(from_attributes=True)