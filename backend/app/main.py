from fastapi import FastAPI
from app.init_db import crear_base_de_datos_si_no_existe, crear_tablas
from contextlib import asynccontextmanager
from app.api import ordenes
from app.api import productos

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    crear_base_de_datos_si_no_existe()
    crear_tablas()
    yield  

app = FastAPI(lifespan=lifespan)
app.include_router(ordenes.router)
app.include_router(productos.router)

@app.get("/")
def index():
    return {"message": "API funcionando correctamente"}