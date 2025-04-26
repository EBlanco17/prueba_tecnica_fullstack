import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.core.database import SessionLocal
from app.models.producto import Producto

"""
Este script se utiliza para cargar productos iniciales en la base de datos.
Es útil para poblar la base de datos con datos de prueba o configuración inicial.
"""

def cargar_productos():
    """
    Inserta una lista de productos predefinidos en la base de datos.

    Los productos incluyen atributos como nombre, cantidad disponible y precio unitario.
    """
    db = SessionLocal()
    productos = [
        Producto(nombre="Teclado mecánico", cantidad_disponible=17, precio_unitario=120.50),
        Producto(nombre="Mouse inalámbrico", cantidad_disponible=21, precio_unitario=45.99),
        Producto(nombre="Monitor 24 pulgadas", cantidad_disponible=30, precio_unitario=800.00),
        Producto(nombre="Laptop gamer", cantidad_disponible=13, precio_unitario=2500.00),
        Producto(nombre="Auriculares bluetooth", cantidad_disponible=6, precio_unitario=75.25),
    ]
    db.add_all(productos)
    db.commit()
    db.close()
    print("Productos insertados correctamente.")

if __name__ == "__main__":
    cargar_productos()