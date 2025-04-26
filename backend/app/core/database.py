from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL

# Configuración de la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

"""
Este módulo configura la conexión a la base de datos utilizando SQLAlchemy.
Define el motor de la base de datos, la sesión local y la clase base para los modelos.
"""