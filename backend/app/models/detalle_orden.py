from sqlalchemy import Column, Integer, Float, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.orden import Orden  # Importación para type hints

class DetalleOrden(Base):
    __tablename__ = "detalle_orden"

    id: int = Column(Integer, primary_key=True, index=True)
    orden_id: int = Column(Integer, ForeignKey("orden.id", ondelete="CASCADE"), nullable=False)
    producto_id: int = Column(Integer, ForeignKey("producto.id", ondelete="CASCADE"), nullable=False)
    cantidad: int = Column(Integer, nullable=False)
    precio_unitario: float = Column(Float, nullable=False)
    subtotal: float = Column(Float, nullable=False)

    orden: "Orden" = relationship("Orden", back_populates="detalles")