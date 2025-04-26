from dotenv import load_dotenv
import os

load_dotenv()

# Variables de entorno para la configuración de la base de datos
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL_WITHOUT_DB = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"
DATABASE_URL = f"{DATABASE_URL_WITHOUT_DB}{DB_NAME}"

"""
Este módulo carga las variables de entorno necesarias para la configuración
de la base de datos y construye la URL de conexión.
"""