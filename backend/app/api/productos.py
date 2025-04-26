from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import SessionLocal
from app.models.producto import Producto
from app.models.detalle_orden import DetalleOrden
from app.schemas.producto import ProductoTopOut

router = APIRouter(prefix="/productos", tags=["Productos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/top3", response_model=list[ProductoTopOut])
def obtener_top_3(db: Session = Depends(get_db)):
    resultados = (
        db.query(
            Producto.nombre.label("nombre"),
            func.sum(DetalleOrden.cantidad).label("total_comprado")
        )
        .join(DetalleOrden, Producto.id == DetalleOrden.producto_id)
        .group_by(Producto.id)
        .order_by(func.sum(DetalleOrden.cantidad).desc())
        .limit(3)
        .all()
    )
    return resultados
