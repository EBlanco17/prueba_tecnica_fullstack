from pydantic import BaseModel, Field, ConfigDict

class ProductoBase(BaseModel):
    nombre: str
    cantidad_disponible: int = Field(gt=-1)
    precio_unitario: float = Field(gt=0)

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)  

class ProductoTopOut(BaseModel):
    nombre: str
    total_comprado: int

    model_config = ConfigDict(from_attributes=True)  