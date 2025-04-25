from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Producto(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    cantidad_disponible = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
