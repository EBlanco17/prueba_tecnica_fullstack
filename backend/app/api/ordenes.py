from fastapi import APIRouter, Depends, HTTPException, status
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
    # Validar que la orden tenga al menos un producto
    if not orden.detalles or len(orden.detalles) == 0:
        raise HTTPException(
            status_code=400, detail="No se puede crear una orden sin productos."
        )

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

@router.get("/", response_model=list[OrdenOut])
def listar_ordenes(db: Session = Depends(get_db)):
    ordenes = db.query(model_orden.Orden).all()
    for orden in ordenes:
        orden.detalles 
    return ordenes

@router.get("/{orden_id}", response_model=OrdenOut)
def obtener_orden(orden_id: int, db: Session = Depends(get_db)):
    orden = db.query(model_orden.Orden).filter(model_orden.Orden.id == orden_id).first()
    if not orden:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Orden no encontrada")
    return orden

@router.delete("/{orden_id}", status_code=204)
def eliminar_orden(orden_id: int, db: Session = Depends(get_db)):
    orden = db.query(model_orden.Orden).filter(model_orden.Orden.id == orden_id).first()
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")

    for detalle in orden.detalles:
        producto = db.query(model_producto.Producto).filter(model_producto.Producto.id == detalle.producto_id).first()
        if producto:
            producto.cantidad_disponible += detalle.cantidad

    db.delete(orden)
    db.commit()
    return

@router.put("/{orden_id}", response_model=OrdenOut)
def actualizar_orden(orden_id: int, nueva_orden: OrdenCreate, db: Session = Depends(get_db)):
    orden = db.query(model_orden.Orden).filter(model_orden.Orden.id == orden_id).first()
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")

    # Revertir el stock de los productos y eliminar los detalles existentes
    for detalle in orden.detalles:
        producto = db.query(model_producto.Producto).filter(model_producto.Producto.id == detalle.producto_id).first()
        if producto:
            producto.cantidad_disponible += detalle.cantidad
        db.delete(detalle)

    total = 0
    nuevos_detalles = []
    for d in nueva_orden.detalles:
        producto = db.query(model_producto.Producto).filter(model_producto.Producto.id == d.producto_id).first()
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        if producto.cantidad_disponible < d.cantidad:
            raise HTTPException(status_code=400, detail="Stock insuficiente")

        # Actualizar el precio unitario del producto si se proporciona en la solicitud
        if d.precio_unitario is not None and d.precio_unitario >= 0:
            producto.precio_unitario = d.precio_unitario

        producto.cantidad_disponible -= d.cantidad
        subtotal = d.cantidad * producto.precio_unitario
        nuevo_detalle = model_detalle.DetalleOrden(
            orden_id=orden.id,
            producto_id=d.producto_id,
            cantidad=d.cantidad,
            precio_unitario=producto.precio_unitario,
            subtotal=subtotal
        )
        nuevos_detalles.append(nuevo_detalle)
        total += subtotal
        db.add(nuevo_detalle)

    orden.total = total
    db.commit()
    db.refresh(orden)
    return orden
