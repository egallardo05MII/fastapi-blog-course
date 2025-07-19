from typing import Optional
from pydantic import BaseModel, model_validator, ConfigDict  # Nuevo import aquí
from datetime import datetime


class CreateBlog(BaseModel):
    title:str
    slug: str
    content: Optional[str] = None

    @model_validator(mode='before')  # Reemplazo de root_validator
    def generate_slug(cls, values: dict) -> dict:
        if 'title' in values:
            values["slug"]=values.get("title").replace(" ","-").lower()
            return values

class UpdateBlog(CreateBlog):
    pass 


class ShowBlog(BaseModel):
    title: str
    content: Optional[str] = None  # Mejor práctica: valor por defecto explícito
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)  # ¡Sintaxis nueva!
    #class Config():
    #    from_attributes = True  # Nuevo nombre para orm_mode en Pydantic v2
        
            