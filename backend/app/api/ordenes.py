from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.orden import OrdenCreate, OrdenOut
from app.core.database import SessionLocal
from app.models import orden as model_orden
from app.models import detalle_orden as model_detalle
from app.models import producto as model_producto

router = APIRouter(prefix="/ordenes", tags=["Ordenes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrdenOut)
def crear_orden(orden: OrdenCreate, db: Session = Depends(get_db)):
    total = 0
    nueva_orden = model_orden.Orden(total=0)
    db.add(nueva_orden)
    db.commit()
    db.refresh(nueva_orden)

    detalles = []
    for d in orden.detalles:
        producto = db.query(model_producto.Producto).filter(model_producto.Producto.id == d.producto_id).first()
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        if producto.cantidad_disponible < d.cantidad:
            raise HTTPException(status_code=400, detail="Stock insuficiente")
        
        producto.cantidad_disponible -= d.cantidad
        subtotal = d.cantidad * producto.precio_unitario
        detalle = model_detalle.DetalleOrden(
            orden_id=nueva_orden.id,
            producto_id=d.producto_id,
            cantidad=d.cantidad,
            precio_unitario=producto.precio_unitario,
            subtotal=subtotal
        )
        total += subtotal
        detalles.append(detalle)
        db.add(detalle)

    nueva_orden.total = total
    db.commit()
    db.refresh(nueva_orden)
    return nueva_orden
