from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Producto(Base):
    """
    Modelo que representa un producto en la base de datos.

    Atributos:
        id (int): Identificador único del producto.
        nombre (str): Nombre del producto.
        cantidad_disponible (int): Cantidad disponible en inventario.
        precio_unitario (float): Precio unitario del producto.
    """
    __tablename__ = "producto"

    id: int = Column(Integer, primary_key=True, index=True)
    nombre: str = Column(String(100), nullable=False)
    cantidad_disponible: int = Column(Integer, nullable=False)
    precio_unitario: float = Column(Float, nullable=False)