from pydantic import BaseModel, EmailStr, Field, ConfigDict  # Nuevo import

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)

class ShowUser(BaseModel):
    id: int
    email:EmailStr
    is_active:bool

    model_config = ConfigDict(from_attributes=True)  # ¡Sintaxis nueva!
    #class Config():
    #    from_attributes = True  # ← Nuevo nombre
