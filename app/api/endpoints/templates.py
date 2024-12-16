from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.template import Template, TemplateCreate, TemplateUpdate
from app.models.template import Template as TemplateModel
from app.schemas.user import User

router = APIRouter()

@router.post("/", response_model=Template)
def create_template(
    *,
    db: Session = Depends(get_db),
    template_in: TemplateCreate,
    current_user: User = Depends(get_current_user)
):
    template = TemplateModel(
        name=template_in.name,
        tag=template_in.tag,
        template_code=template_in.template_code
    )
    db.add(template)
    db.commit()
    db.refresh(template)
    return template

@router.get("/", response_model=List[Template])
def read_templates(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user)
):
    templates = db.query(TemplateModel).offset(skip).limit(limit).all()
    return templates

@router.get("/{template_id}", response_model=Template)
def read_template(
    *,
    db: Session = Depends(get_db),
    template_id: int,
    current_user: User = Depends(get_current_user)
):
    template = db.query(TemplateModel).filter(TemplateModel.id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template

@router.put("/{template_id}", response_model=Template)
def update_template(
    *,
    db: Session = Depends(get_db),
    template_id: int,
    template_in: TemplateUpdate,
    current_user: User = Depends(get_current_user)
):
    template = db.query(TemplateModel).filter(TemplateModel.id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    
    update_data = template_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(template, field, value)
    
    db.add(template)
    db.commit()
    db.refresh(template)
    return template

@router.delete("/{template_id}", response_model=Template)
def delete_template(
    *,
    db: Session = Depends(get_db),
    template_id: int,
    current_user: User = Depends(get_current_user)
):
    template = db.query(TemplateModel).filter(TemplateModel.id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    
    db.delete(template)
    db.commit()
    return template
