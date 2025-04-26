from typing import Generator, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import SessionLocal
from app.models.producto import Producto
from app.models.detalle_orden import DetalleOrden
from app.schemas.producto import ProductoOut, ProductoTopOut
from fastapi.responses import FileResponse
from app.pdf.generate_pdf import generar_reporte_pdf

router: APIRouter = APIRouter(prefix="/productos", tags=["Productos"])

def get_db() -> Generator[Session, None, None]:
    """
    Generador para obtener una sesión de base de datos.
    Cierra la sesión automáticamente después de su uso.

    Returns:
        Generator[Session, None, None]: Sesión de base de datos.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ProductoOut])
def obtener_productos(db: Session = Depends(get_db)) -> List[ProductoOut]:
    """
    Obtiene la lista de todos los productos en la base de datos.

    Args:
        db (Session): Sesión de base de datos.

    Returns:
        List[ProductoOut]: Lista de productos.
    """
    productos: List[Producto] = db.query(Producto).all()
    return [ProductoOut.from_orm(producto) for producto in productos]

@router.get("/top3", response_model=List[ProductoTopOut])
def obtener_top_3(db: Session = Depends(get_db)) -> List[ProductoTopOut]:
    """
    Obtiene los 3 productos más vendidos.

    Args:
        db (Session): Sesión de base de datos.

    Returns:
        List[ProductoTopOut]: Lista de los 3 productos más vendidos.
    """
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
    return [ProductoTopOut(nombre=r.nombre, total_comprado=r.total_comprado) for r in resultados]

@router.get("/top3/pdf", response_class=FileResponse)
def descargar_pdf_top3(db: Session = Depends(get_db)) -> FileResponse:
    """
    Genera y descarga un reporte en PDF de los 3 productos más vendidos.

    Args:
        db (Session): Sesión de base de datos.

    Returns:
        FileResponse: Archivo PDF generado con los datos de los productos más vendidos.
    """
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

    productos: List[dict] = [
        {
            "nombre": r.nombre,
            "total_comprado": int(r.total_comprado),
            "precio_unitario": float(r.precio_unitario)
        } for r in resultados
    ]

    pdf_path: str = generar_reporte_pdf(productos)
    return FileResponse(pdf_path, media_type="application/pdf", filename="top3_productos.pdf")