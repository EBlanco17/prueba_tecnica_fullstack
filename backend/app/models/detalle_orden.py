from sqlalchemy import Column, Integer, Float, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship, Mapped
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.orden import Orden

class DetalleOrden(Base):
    """
    Modelo que representa el detalle de una orden en la base de datos.

    Atributos:
        id (int): Identificador único del detalle de la orden.
        orden_id (int): Identificador de la orden asociada.
        producto_id (int): Identificador del producto asociado.
        cantidad (int): Cantidad del producto en la orden.
        precio_unitario (float): Precio unitario del producto.
        subtotal (float): Subtotal calculado como cantidad * precio_unitario.
        orden (Orden): Relación con el modelo de la orden.
    """
    __tablename__ = "detalle_orden"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    orden_id: Mapped[int] = Column(Integer, ForeignKey("orden.id", ondelete="CASCADE"), nullable=False)
    producto_id: Mapped[int] = Column(Integer, ForeignKey("producto.id", ondelete="CASCADE"), nullable=False)
    cantidad: Mapped[int] = Column(Integer, nullable=False)
    precio_unitario: Mapped[float] = Column(Float, nullable=False)
    subtotal: Mapped[float] = Column(Float, nullable=False)

    orden: Mapped["Orden"] = relationship("Orden", back_populates="detalles")