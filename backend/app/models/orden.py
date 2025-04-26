from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship, Mapped
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.detalle_orden import DetalleOrden

class Orden(Base):
    __tablename__ = "orden"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    fecha: Mapped[DateTime] = Column(DateTime(timezone=True), server_default=func.now())
    total: Mapped[float] = Column(Float, nullable=False)

    detalles: Mapped[list["DetalleOrden"]] = relationship(
        "DetalleOrden", back_populates="orden", cascade="all, delete-orphan"
    )