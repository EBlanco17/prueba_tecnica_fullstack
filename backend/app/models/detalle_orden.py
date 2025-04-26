from sqlalchemy import Column, Integer, Float, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship, Mapped
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.orden import Orden

class DetalleOrden(Base):
    __tablename__ = "detalle_orden"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    orden_id: Mapped[int] = Column(Integer, ForeignKey("orden.id", ondelete="CASCADE"), nullable=False)
    producto_id: Mapped[int] = Column(Integer, ForeignKey("producto.id", ondelete="CASCADE"), nullable=False)
    cantidad: Mapped[int] = Column(Integer, nullable=False)
    precio_unitario: Mapped[float] = Column(Float, nullable=False)
    subtotal: Mapped[float] = Column(Float, nullable=False)

    orden: Mapped["Orden"] = relationship("Orden", back_populates="detalles")