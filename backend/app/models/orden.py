from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
from app.models.detalle_orden import DetalleOrden
from sqlalchemy.orm import relationship
class Orden(Base):
    __tablename__ = "orden"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    total = Column(Float, nullable=False)

    detalles = relationship("DetalleOrden", back_populates="orden", cascade="all, delete-orphan")