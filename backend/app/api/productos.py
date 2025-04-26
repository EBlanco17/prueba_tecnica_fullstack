from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import SessionLocal
from app.models.producto import Producto
from app.models.detalle_orden import DetalleOrden
from app.schemas.producto import ProductoTopOut
from fastapi.responses import FileResponse
from app.pdf.generate_pdf import generar_reporte_pdf

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

@router.get("/top3/pdf", response_class=FileResponse)
def descargar_pdf_top3(db: Session = Depends(get_db)):
    resultados = (
        db.query(
            Producto.nombre.label("nombre"),
            func.sum(DetalleOrden.cantidad).label("total_comprado"),
            Producto.precio_unitario
        )
        .join(DetalleOrden, Producto.id == DetalleOrden.producto_id)
        .group_by(Producto.id)
        .order_by(func.sum(DetalleOrden.cantidad).desc())
        .limit(3)
        .all()
    )

    productos = [
        {
            "nombre": r.nombre,
            "total_comprado": int(r.total_comprado),
            "precio_unitario": float(r.precio_unitario)
        } for r in resultados
    ]

    pdf_path = generar_reporte_pdf(productos)
    return FileResponse(pdf_path, media_type="application/pdf", filename="top3_productos.pdf")