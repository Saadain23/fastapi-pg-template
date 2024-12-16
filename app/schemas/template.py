from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class TemplateBase(BaseModel):
    name: str
    tag: str
    template_code: str

class TemplateCreate(TemplateBase):
    pass

class TemplateUpdate(BaseModel):
    name: Optional[str] = None
    tag: Optional[str] = None
    template_code: Optional[str] = None

class Template(TemplateBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True