from sqlalchemy import Column, Integer, Float, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship
class DetalleOrden(Base):
    __tablename__ = "detalle_orden"

    id = Column(Integer, primary_key=True, index=True)
    orden_id = Column(Integer, ForeignKey("orden.id", ondelete="CASCADE"), nullable=False)
    producto_id = Column(Integer, ForeignKey("producto.id", ondelete="CASCADE"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)

    orden = relationship("Orden", back_populates="detalles")