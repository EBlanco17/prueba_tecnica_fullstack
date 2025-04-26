import pymysql
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from app.core.config import DATABASE_URL_WITHOUT_DB, DB_NAME
from app.core.database import Base
from app.models.producto import Producto
from app.models.orden import Orden
from app.models.detalle_orden import DetalleOrden
import os

"""
Este módulo contiene funciones para inicializar la base de datos.

Incluye la creación de la base de datos si no existe y la creación de las tablas
definidas en los modelos.
"""

def crear_base_de_datos_si_no_existe() -> None:
    """
    Crea la base de datos si no existe.

    Conecta al servidor de base de datos utilizando las credenciales configuradas
    y ejecuta un comando SQL para crear la base de datos si aún no está creada.
    """
    conn: pymysql.connections.Connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    cursor: pymysql.cursors.Cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.commit()
    cursor.close()
    conn.close()

def crear_tablas() -> None:
    """
    Crea las tablas en la base de datos.

    Utiliza SQLAlchemy para crear todas las tablas definidas en los modelos
    si estas no existen en la base de datos.
    """
    engine: Engine = create_engine(f"{DATABASE_URL_WITHOUT_DB}{DB_NAME}")
    Base.metadata.create_all(bind=engine)