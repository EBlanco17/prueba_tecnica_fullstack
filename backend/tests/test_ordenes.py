import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import SessionLocal
from app.models import producto as model_producto
from app.models import orden as model_orden
from app.models import detalle_orden as model_detalle

client = TestClient(app)

@pytest.fixture
def setup_db():
    """Fixture para configurar la base de datos antes de las pruebas."""
    db = SessionLocal()
    # Crear productos de prueba
    producto1 = model_producto.Producto(id=1, nombre="Producto 1", cantidad_disponible=10, precio_unitario=100)
    producto2 = model_producto.Producto(id=2, nombre="Producto 2", cantidad_disponible=5, precio_unitario=200)
    db.add(producto1)
    db.add(producto2)
    db.commit()
    yield
    # Limpiar la base de datos después de las pruebas
    db.query(model_detalle.DetalleOrden).delete()  # Eliminar detalles de órdenes
    db.query(model_orden.Orden).delete()          # Eliminar órdenes
    db.query(model_producto.Producto).delete()    # Eliminar productos
    db.commit()
    db.close()

def test_crear_orden(setup_db):
    """Prueba para crear una orden."""
    payload = {
        "detalles": [
            {"producto_id": 1, "cantidad": 2},
            {"producto_id": 2, "cantidad": 1}
        ]
    }
    response = client.post("/ordenes/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 400  # 2*100 + 1*200
    assert len(data["detalles"]) == 2

def test_crear_orden_sin_productos():
    """Prueba para crear una orden sin productos."""
    payload = {"detalles": []}
    response = client.post("/ordenes/", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "No se puede crear una orden sin productos."

def test_obtener_orden(setup_db):
    """Prueba para obtener una orden existente."""
    # Crear una orden primero
    payload = {
        "detalles": [
            {"producto_id": 1, "cantidad": 1}
        ]
    }
    response = client.post("/ordenes/", json=payload)
    orden_id = response.json()["id"]

    # Obtener la orden
    response = client.get(f"/ordenes/{orden_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == orden_id

def test_actualizar_orden(setup_db):
    """Prueba para actualizar una orden existente."""
    # Crear una orden primero
    payload = {
        "detalles": [
            {"producto_id": 1, "cantidad": 1}
        ]
    }
    response = client.post("/ordenes/", json=payload)
    orden_id = response.json()["id"]

    # Actualizar la orden
    update_payload = {
        "detalles": [
            {"producto_id": 2, "cantidad": 2}
        ]
    }
    response = client.put(f"/ordenes/{orden_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 400  # 2*200

def test_eliminar_orden(setup_db):
    """Prueba para eliminar una orden existente."""
    # Crear una orden primero
    payload = {
        "detalles": [
            {"producto_id": 1, "cantidad": 1}
        ]
    }
    response = client.post("/ordenes/", json=payload)
    orden_id = response.json()["id"]

    # Eliminar la orden
    response = client.delete(f"/ordenes/{orden_id}")
    assert response.status_code == 204

    # Verificar que la orden ya no existe
    response = client.get(f"/ordenes/{orden_id}")
    assert response.status_code == 404