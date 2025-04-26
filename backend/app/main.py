from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.init_db import crear_base_de_datos_si_no_existe, crear_tablas
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from app.api import ordenes, productos

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Context manager para el ciclo de vida de la aplicación.
    Se encarga de crear la base de datos y las tablas si no existen.
    """
    crear_base_de_datos_si_no_existe()
    crear_tablas()
    yield  

app: FastAPI = FastAPI(lifespan=lifespan)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Cambia esto si tu frontend está en otro origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(ordenes.router)
app.include_router(productos.router)

@app.get("/")
def index() -> dict:
    """
    Endpoint raíz de la API.
    Retorna un mensaje indicando que la API está funcionando correctamente.
    """
    return {"message": "API funcionando correctamente"}